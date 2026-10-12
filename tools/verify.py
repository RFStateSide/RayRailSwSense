"""Verify the prepared source, manufacturing correspondence and exact-byte manifest."""
from pathlib import Path
import argparse,json,re,csv,math,collections,subprocess,tempfile,xml.etree.ElementTree as ET,runpy,hashlib
ROOT=Path(__file__).resolve().parents[1]
def parse(s):
 stack=[];root=None
 for v in re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',s):
  if v=='(':
   a=[]
   if stack:stack[-1].append(a)
   stack.append(a)
  elif v==')':root=stack.pop()
  else:stack[-1].append(json.loads(v) if v.startswith('"') else v)
 return root
def nodes(a,k):return [v for v in a if isinstance(v,list) and v and v[0]==k]
def one(a,k):return next(iter(nodes(a,k)),[])
def prop(a,k):return next((v[2] for v in nodes(a,'property') if v[1]==k),'')
def point(f,p):
 at=one(f,'at');x,y=map(float,at[1:3]);ang=math.radians(float(at[3]) if len(at)>3 else 0)
 px,py=map(float,one(p,'at')[1:3])
 return (x+px*math.cos(ang)+py*math.sin(ang),y-px*math.sin(ang)+py*math.cos(ang))
def drill_points(text):
 tools={};diam=None;points=[];scale=25.4 if 'INCH' in text else 1
 for line in text.splitlines():
  m=re.fullmatch(r'T(\d+)C([\d.]+)',line)
  if m:tools[m[1]]=float(m[2])*scale;continue
  m=re.fullmatch(r'T(\d+)',line)
  if m:diam=tools[m[1]];continue
  m=re.fullmatch(r'X(-?[\d.]+)Y(-?[\d.]+)',line)
  if m:points.append((float(m[1])*scale,-float(m[2])*scale,diam))
 return points
def match_points(actual,expected,tolerance):
 remaining=list(set(expected))
 assert len(actual)==len(remaining),('Hole counts',len(actual),len(remaining))
 for h in actual:
  q=next((p for p in remaining if all(abs(a-b)<=tolerance for a,b in zip(h,p))),None)
  assert q is not None,('Hole mismatch',h)
  remaining.remove(q)
def gerber_pads(text):
 result=[];pin=None;net=None
 for line in text.splitlines():
  if line.startswith('%TO.P,'):
   fields=line.split('*')[0].split(',');pin=tuple(fields[1:3])
  elif line.startswith('%TO.N,'):net=line[6:].split('*')[0]
  elif line.startswith('%TD'):pin=None;net=None
  m=re.fullmatch(r'X(-?\d+)Y(-?\d+)D03\*',line)
  if m and pin:result.append((pin,int(m[1])/1e6,-int(m[2])/1e6,net))
 return result
def geometry(pcb):
 # Excludes metadata/graphics; preserves pad shape, position, rotation, nets,
 # tracks, vias, zone polygons/fills and board outline.
 fps=[]
 for f in nodes(pcb,'footprint'):
  fps.append({'at':one(f,'at'),'pads':nodes(f,'pad')})
 return {'footprints':fps,**{k:nodes(pcb,k) for k in ['segment','via','zone','gr_rect','gr_line','gr_arc']}}
def check(cli):
 board=parse((ROOT/'hardware/RayRailSwSense.kicad_pcb').read_text(encoding='utf8'))
 sch=parse((ROOT/'hardware/RayRailSwSense.kicad_sch').read_text(encoding='utf8'))
 fps={prop(f,'Reference'):f for f in nodes(board,'footprint')}
 syms={prop(f,'Reference'):f for f in nodes(sch,'symbol') if not prop(f,'Reference').startswith('#')}
 assert set(fps)==set(syms)|{'H1','H2','H3','H4'}
 assert len(syms)==15
 assert not nodes(sch,'embedded_files')
 lib=parse((ROOT/'hardware/libraries/RayRailSwSense.kicad_sym').read_text(encoding='utf8'))
 defs={f[1] for f in nodes(lib,'symbol')}
 for f in nodes(sch,'symbol'):assert one(f,'lib_id')[1].split(':')[1] in defs
 for ref,f in fps.items():
  assert not nodes(f,'model')
  assert (ROOT/'hardware/libraries/RayRailSwSense.pretty'/(f[1].split(':')[1]+'.kicad_mod')).exists()
  if ref in syms:
   assert prop(syms[ref],'Value')==prop(f,'Value')
   assert prop(syms[ref],'Footprint')==f[1]
   assert prop(syms[ref],'MPN')==prop(f,'MPN')
 with tempfile.TemporaryDirectory() as t:
  out=Path(t)/'net.xml'
  subprocess.run([cli,'sch','export','netlist','--format','kicadxml','-o',str(out),str(ROOT/'hardware/RayRailSwSense.kicad_sch')],check=True,capture_output=True)
  xml=ET.parse(out).getroot()
  snets={frozenset((n.get('ref'),n.get('pin')) for n in net.findall('node')) for net in xml.findall('./nets/net')}
 bnets=collections.defaultdict(set);pin_nets={};expected_pads={};holes=[]
 for ref,f in fps.items():
  for p in nodes(f,'pad'):
   if one(p,'net') and p[1]:
    net=one(p,'net')[-1]
    if ref in syms:bnets[net].add((ref,p[1]));pin_nets[(ref,p[1])]=net;expected_pads[(ref,p[1])]=(*point(f,p),net)
   if one(p,'drill'):
    drill=one(p,'drill');assert drill[1]!='oval'
    holes.append((*point(f,p),float(drill[1])))
 for v in nodes(board,'via'):holes.append((*map(float,one(v,'at')[1:3]),float(one(v,'drill')[1])))
 assert snets=={frozenset(v) for v in bnets.values()},'Schematic/PCB connectivity differs'
 assert prop(fps['R4'],'Value')=='2k' and prop(fps['R4'],'MPN')=='RMCF1206FT2K00'
 assert prop(fps['U1'],'MPN')=='BTH500301LUAAUMA1'
 assert prop(fps['FB1'],'MPN')=='BLM31PG121SN1L' and prop(fps['FB1'],'Supplier_PN')=='490-1056-1-ND'
 assert prop(fps['F1'],'Value')=='178.6165.0002'
 def same(*pins):assert len({pin_nets[p] for p in pins})==1,pins
 same(('J3','1'),('J2','1'),('U1','5'),('R5','2'))
 same(('J3','2'),('R5','1'),('R6','2'))
 same(('J3','3'),('FB1','2'))
 same(('J3','4'),('R1','1'))
 same(('J3','5'),('R3','1'),('C2','1'))
 same(('J3','6'),('U1','1'),('R4','1'),('R6','1'))
 same(('U1','2'),('R4','2'),('R3','2'))
 man=ROOT/'manufacturing/P2-prep-01'
 found={}
 for pin,x,y,net in gerber_pads((man/'RayRailSwSense-F_Cu.gbr').read_text()):
  if pin in expected_pads:
   ex,ey,en=expected_pads[pin];assert abs(x-ex)<1e-5 and abs(y-ey)<1e-5 and net==en,(pin,'Gerber differs')
   found[pin]=True
 assert set(found)==set(expected_pads)
 drilled=[h for f in man.glob('*.drl') for h in drill_points(f.read_text())]
 match_points(drilled,holes,0.00101)
 rows=list(csv.DictReader((ROOT/'bom/RayRailSwSense.csv').open(encoding='utf8')))
 assert {r['Designator'] for r in rows}==set(syms)
 for row in rows:
  f=fps[row['Designator']];assert row['Quantity']=='1'
  for k in ['Value','MPN','Supplier_PN']:assert row[k]==prop(f,k),(row['Designator'],k)
  assert row['Footprint']==f[1]
 pos=list(csv.DictReader((man/'RayRailSwSense-positions.csv').open(encoding='utf8')))
 assert {r['Ref'] for r in pos}==set(syms)
 for row in pos:
  f=fps[row['Ref']];at=one(f,'at')
  assert row['Val']==prop(f,'Value') and row['Package']==f[1].split(':')[1]
  assert abs(float(row['PosX'])-float(at[1]))<1e-5 and abs(float(row['PosY'])+float(at[2]))<1e-5
  assert abs((float(row['Rot'])-(float(at[3]) if len(at)>3 else 0))%360)<1e-5
 for n in ['LICENSE','NOTICE']:assert (man/n).read_bytes()==(ROOT/n).read_bytes()
 assert (man/'RayRailSwSense-bom.csv').read_bytes()==(ROOT/'bom/RayRailSwSense.csv').read_bytes()
 expected_license=json.loads((ROOT/'docs/license-provenance.json').read_text())['sha256']
 assert hashlib.sha256((ROOT/'LICENSE').read_bytes()).hexdigest()==expected_license
 drc=json.loads((ROOT/'docs/validation/drc.json').read_text())
 assert not drc['violations'] and not drc['unconnected_items'] and not drc['schematic_parity']
 erc=json.loads((ROOT/'docs/validation/erc.json').read_text())
 violations=[v for s in erc['sheets'] for v in s['violations']]
 assert collections.Counter(v['type'] for v in violations)=={'pin_to_pin':18}
 source=json.loads((ROOT/'docs/validation/source-comparison.json').read_text())
 assert hashlib.sha256(json.dumps(geometry(board),sort_keys=True).encode()).hexdigest()==source['release_geometry_sha256']==source['original_geometry_sha256']
 return {'component_references':len(syms),'board_only_mounting_features':4,'schematic_pcb_pin_net_partitions_equal':True,'local_definitions_resolve':True,'bom_and_positions_match':True,'connector_pin_assignments_verified':True,'gerber_component_pad_positions_and_nets':len(found),'drilled_holes':len(drilled),'drill_centers_diameters_match':True,'original_layout_geometry_preserved':True,'drc_violations':0,'unconnected_pcb_items':0,'schematic_parity_issues':0,'retained_erc_pin_type_findings':18}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kicad-cli',default='kicad-cli');p.add_argument('--record',action='store_true');a=p.parse_args()
 result=check(a.kicad_cli)
 if a.record:(ROOT/'docs/validation/checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
 elif (ROOT/'SHA256SUMS').exists():runpy.run_path(str(ROOT/'tools/integrity.py'))['verify'](ROOT)
 print(json.dumps(result,indent=2))
