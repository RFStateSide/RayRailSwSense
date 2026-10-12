"""Generate P2-prep-01 outputs with KiCad 9. Inspect changes and renew SHA256SUMS afterwards."""
from pathlib import Path
import argparse,subprocess,json,shutil
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kicad-cli',default='kicad-cli');a=p.parse_args()
 out='manufacturing/P2-prep-01';board='hardware/RayRailSwSense.kicad_pcb';sch='hardware/RayRailSwSense.kicad_sch'
 for d in [out,'docs/images','docs/validation']:(ROOT/d).mkdir(parents=True,exist_ok=True)
 commands=[
 ['pcb','export','gerbers','--no-protel-ext','--layers','F.Cu,B.Cu,F.Mask,B.Mask,F.Paste,B.Paste,F.SilkS,B.SilkS,Edge.Cuts','-o',out+'/',board],
 ['pcb','export','drill','--excellon-separate-th','--excellon-units','mm','-o',out+'/',board],
 ['pcb','export','pos','--format','csv','--units','mm','-o',out+'/RayRailSwSense-positions.csv',board],
 ['sch','export','svg','-o','docs/images/',sch],
 ['pcb','export','svg','--mode-single','--fit-page-to-board','--exclude-drawing-sheet','--layers','F.Cu,F.SilkS,Edge.Cuts','-o','docs/images/pcb-front.svg',board],
 ['pcb','drc','--schematic-parity','--format','json','-o','docs/validation/drc.json',board],
 ['sch','erc','--format','json','-o','docs/validation/erc.json',sch]]
 for cmd in commands:
  r=subprocess.run([a.kicad_cli]+cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf8',errors='replace')
  if r.returncode:raise RuntimeError(str(cmd)+'\n'+r.stdout+r.stderr)
  print('Completed: '+' '.join(cmd[:3]))
 def scrub(x):
  if isinstance(x,str):return x.replace(str(ROOT),'$PROJECT').replace(ROOT.as_posix(),'$PROJECT')
  if isinstance(x,list):return [scrub(v) for v in x]
  if isinstance(x,dict):return {k:scrub(v) for k,v in x.items()}
  return x
 for n in ['drc','erc']:
  f=ROOT/'docs/validation'/(n+'.json');f.write_text(json.dumps(scrub(json.loads(f.read_text(encoding='utf8'))),indent=2)+'\n',encoding='utf8')
 for n in ['LICENSE','NOTICE']:shutil.copyfile(ROOT/n,ROOT/out/n)
 shutil.copyfile(ROOT/'bom/RayRailSwSense.csv',ROOT/out/'RayRailSwSense-bom.csv')
 (ROOT/'docs/validation/generation.json').write_text(json.dumps({'revision':'P2-prep-01','tool':subprocess.check_output([a.kicad_cli,'version'],text=True).strip(),'commands':commands},indent=2)+'\n',encoding='utf8')
if __name__=='__main__':main()
