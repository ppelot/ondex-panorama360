/* ============================================================
   Zone kits — building materials (PVC sheets): extrusion plant,
   builders' merchant + DIY store, roofing site, farm & greenhouses.
   Authored for the ONDEX world; generic enough for any maker of
   roofing, cladding or sheet products.
   ============================================================ */
/* ---------- props ---------- */
/* a pallet with a bundle of sheets; corrugation ridges on top */
function sheetStack(g,x,z,w,d,h,col){g.box(x-w/2,0,z-d/2,x+w/2,.15,z+d/2,P.WOOD);g.rbox(x-w/2+.05,.15,z-d/2+.05,x+w/2-.05,.15+h,z+d/2-.05,.04,col,col);
  for(let k=z-d/2+.25;k<z+d/2-.2;k+=.4)g.box(x-w/2+.1,.15+h,k,x+w/2-.1,.15+h+.05,k+.14,col);}
/* sheet extrusion + bi-orientation line, running west → east at z */
function extrusionLine(g,x0,x1,z){
  g.rbox(x0,0,z-1.6,x0+4.6,1.6,z+1.6,.1,P.MID,P.LIGHT);g.rbox(x0+.4,1.6,z-1.1,x0+3,3.1,z+1.1,.1,P.BR,P.BR);
  g.lathe([x0+4.6,2.1,z],[1,0,0],[[0,0],[.45,0],[.45,7.4],[0,7.4]],10,P.STEEL);
  for(let k=0;k<5;k++)g.lathe([x0+5.2+k*1.3,2.1,z],[1,0,0],[[.62,0],[.62,.8]],10,P.DARK);
  g.lathe([x0+6.6,2.5,z],[0,1,0],[[.25,0],[1.15,1.7],[1.15,2.9],[0,2.95]],12,P.LIGHT);
  g.tube([x0+8.2,1.1,z+2.8],[x0+11,2.1,z+.7],.3,8,P.STEEL);g.rbox(x0+6.4,0,z+2.2,x0+9,1.1,z+3.6,.08,P.MID,P.LIGHT);
  g.rbox(x0+12,.9,z-1.8,x0+13.4,3.1,z+1.8,.1,P.DARK,P.MID);
  for(const dx of[14.2,15.4,16.6])g.lathe([x0+dx,2.1,z-1.75],[0,0,1],[[0,0],[.5,0],[.5,3.5],[0,3.5]],12,P.CHROME);
  g.box(x0+13.4,1.2,z-1.3,x1-6,1.28,z+1.3,P.WHITE);
  for(let x=x0+14;x<x1-6;x+=3)for(const s of[-1.4,1.4])g.box(x-.06,0,z+s-.06,x+.06,1.2,z+s+.06,P.MID);
  g.rbox(x0+19,0,z-2.4,x0+31,2.8,z+2.4,.12,P.LIGHT,P.MID);g.box(x0+19,2.1,z+2.4,x0+31,2.45,z+2.48,P.BY);g.box(x0+19,2.1,z-2.48,x0+31,2.45,z-2.4,P.BY);
  for(let k=0;k<4;k++)g.lathe([x0+33+k*1.25,1.65,z-1.6],[0,0,1],[[0,0],[.34,0],[.34,3.2],[0,3.2]],10,P.STEEL);
  g.rbox(x1-6,0,z-1.6,x1-4.6,2.6,z+1.6,.08,P.BY,P.DARK);g.box(x1-6.1,2.6,z-1.7,x1-4.5,2.75,z+1.7,P.MID);
  sheetStack(g,x1-2.2,z,2.6,2.4,1.1,P.WHITE);}
/* multi-span greenhouse: walls and spans of light panels; cut (if any) gets the roof and the camera-facing walls */
function greenhouse(g,cut,x0,z0,x1,z1,h,span){const C=cut||g,n=Math.max(1,Math.round((x1-x0)/span)),sw=(x1-x0)/n,rh=sw*.24;
  g.box(x0,0,z0,x1,h,z0+.12,P.CHROME,P.WHITE);g.box(x0,0,z0,x0+.12,h,z1,P.CHROME,P.WHITE);
  C.box(x0,0,z1-.12,x1,h,z1,P.CHROME,P.WHITE);C.box(x1-.12,0,z0,x1,h,z1,P.CHROME,P.WHITE);
  for(let i=0;i<n;i++){const a=x0+i*sw,b=a+sw;C.gable(a,z0,b,z1,h,rh,P.CHROME,P.CHROME,false);C.box((a+b)/2-.08,h+rh-.02,z0,(a+b)/2+.08,h+rh+.1,z1,P.WHITE);
    C.box(b-.1,h-.1,z0,b+.1,h+.08,z1,P.WHITE);}
  for(let z=z0;z<=z1+.01;z+=(z1-z0)/6)C.box(x1-.02,0,z-.06,x1+.06,h,z+.06,P.WHITE);
  for(let x=x0;x<=x1+.01;x+=sw/2)C.box(x-.06,0,z1-.02,x+.06,h,z1+.06,P.WHITE);}
/* truck crane (boom in local +x, raised by ang), yellow, a bundle of sheets on the hook */
function truckCrane(g,x,z,ry=0,L=34,ang=.85){g.push().tf(x,0,z,ry);const Y=P.YLINE;
  g.rbox(-5,.7,-1.3,5,1.6,1.3,.15,Y,Y);for(const wx of[-3.6,-2.2,2.4,3.8]){wheel(g,wx,1.15,.55,.4);wheel(g,wx,-1.15,.55,.4);}
  g.rbox(3.2,1.6,-1.2,5,3.3,.1,.15,Y,Y);g.box(4.98,2.3,-1.1,5.02,3.1,0,P.GLASS);
  for(const[a,b]of[[-4.4,-1.3],[4.4,-1.3],[-4.4,1.3],[4.4,1.3]]){g.box(a-.15,.5,b*1.6-.15,a+.15,1.3,b*1.6+.15,P.DARK);g.box(a-.4,0,b*1.6-.4,a+.4,.12,b*1.6+.4,P.WOOD);}
  g.cyl(-1,0,1.6,1.4,.5,16,P.DARK);g.rbox(-3,2.1,-1.1,1,3.4,1.1,.12,Y,Y);
  const bx=-.5,by=3.2,tx=bx+Math.cos(ang)*L,ty=by+Math.sin(ang)*L;
  g.tube([bx,by,0],[bx+(tx-bx)*.55,by+(ty-by)*.55,0],.55,6,Y,Y,false);g.tube([bx+(tx-bx)*.5,by+(ty-by)*.5,0],[tx,ty,0],.36,6,Y,Y,false);
  g.tube([tx,ty,0],[tx,ty-12,0],.03,4,P.DARK,P.DARK,false);g.rbox(tx-.35,ty-13,-.3,tx+.35,ty-12,.3,.06,Y,P.DARK);
  g.tube([tx-.1,ty-13,0],[tx-1.2,ty-14.6,0],.02,3,P.DARK,P.DARK,false);g.tube([tx+.1,ty-13,0],[tx+1.2,ty-14.6,0],.02,3,P.DARK,P.DARK,false);
  g.push().tf(tx,ty-15.6,0);sheetStack(g,0,0,4.4,1.2,.75,P.WHITE);g.pop();g.pop();}
/* flatbed truck with sheet bundles (front +x) */
function flatbedStatic(g,x,z,yaw,cab=P.WHITE,load=P.WHITE){g.push().tf(x,0,z,yaw);mkTractor(g,cab);g.push().tf(.35,0,0);
  g.rbox(-12.4,1.2,-1.26,-.6,1.5,1.26,.05,P.DARK,P.WOOD);g.box(-11.8,.95,-.46,-.4,1.25,.46,P.DARK);for(const xx of[-9.0,-10.3,-11.6]){wheel(g,xx,1.0,.5,.42);wheel(g,xx,-1.0,.5,.42);}
  for(const bx of[-11,-7.6,-4.2]){g.push().tf(bx,1.5,0);sheetStack(g,0,0,3,2.3,1.1,load);g.pop();}g.pop();g.pop();}

/* pallet racks holding sheet bundles */
function sheetRack(g,x0,x1,z,levels=3,seed=1){const bays=Math.floor((x1-x0)/2.8),R=rng(seed),C=[P.WHITE,P.CHROME,P.FB,P.CA,P.WHITE];
  for(let i=0;i<=bays;i++){const x=x0+i*2.8;for(const s of[-1,1])g.box(x-.06,0,z+s*.62-.06,x+.06,levels*2.3+.4,z+s*.62+.06,P.RACK);
    for(let l=0;l<levels;l++)g.box(x-.03,.3+l*2.3,z-.62,x+.03,.36+l*2.3,z+.62,P.RACK);}
  for(let l=0;l<levels;l++)for(const s of[-1,1])g.box(x0,.2+l*2.3,z+s*.62-.07,x0+bays*2.8,.36+l*2.3,z+s*.62+.07,P.VEST);
  for(let i=0;i<bays;i++)for(let l=0;l<levels;l++){if(R()<.12)continue;g.push().tf(x0+1.4+i*2.8,.36+l*2.3,z);sheetStack(g,0,0,2.5,1.15,.6+R()*.9,C[(i+l*2)%5]);g.pop();}}
/* cut-away stock building (no roof, no south wall) with sheet racks, docks on the east wall, a glass shipping office */
function sheetWarehouse(g,x,z,sign){g.push().tf(x,0,z);const w=64,d=36,h=11;
  g.rbox(-w/2,0,-d/2,w/2,.3,d/2,.08,P.CONC,P.LIGHT);
  for(const zz of[-6,2,10])g.box(-w/2+2,.31,zz-1.7,w/2-9,.33,zz-1.5,P.YLINE);
  g.rbox(-w/2,0,-d/2,w/2,h,-d/2+.6,.1,P.WHITE,P.BY);g.rbox(-w/2,0,-d/2,-w/2+.6,h,d/2,.1,P.WHITE,P.BY);g.rbox(w/2-.6,0,-d/2,w/2,h,d/2,.1,P.WHITE,P.BY);
  g.box(-w/2,0,d/2-.6,w/2,1.1,d/2,P.WHITE,P.BY);
  for(const[px,s]of[[w/2+.02,1],[-w/2-.02,-1]]){g.decal([px,h*.5,0],[0,0,-s],[0,1,0],d-2,h-1.5,[s,0,0],UV.RIBS,P.WHITE);}
  g.decal([0,h*.5,-d/2-.02],[-1,0,0],[0,1,0],w-2,h-1.5,[0,0,-1],UV.RIBS,P.WHITE);
  g.box(w/2,h-2.6,-d/2-.1,w/2+.1,h-.2,d/2+.1,P.BY);g.decal([w/2+.12,h-1.4,-4],[0,0,-1],[0,1,0],6.6,2.2,[1,0,0],UV.LOGOW,P.BY);
  g.decal([w/2+.12,h-1.4,9],[0,0,-1],[0,1,0],14,1.75,[1,0,0],sign,P.BY);
  for(const dz of[-12,-4.5,3])g.decal([w/2+.12,2.4,dz],[0,0,-1],[0,1,0],4.2,4.4,[1,0,0],UV.DOOR,P.WHITE);
  for(const dz of[-12,-4.5,3])g.box(w/2,0,dz-2.4,w/2+1.8,1.3,dz+2.4,P.CONC);
  for(let k=-d/2+3;k<d/2-2;k+=6.5)g.box(-.25,0,k-.25,.25,h,k+.25,P.STEEL);
  sheetRack(g,-w/2+3,w/2-12,-13,3,2);sheetRack(g,-w/2+3,w/2-12,-8,3,3);sheetRack(g,-w/2+3,w/2-12,1,3,4);sheetRack(g,-w/2+3,w/2-12,6,3,5);
  g.rbox(w/2-10,0,d/2-9,w/2-1.5,3.6,d/2-1.5,.08,P.GLASS,P.WHITE);g.box(w/2-10.05,3.3,d/2-9.05,w/2-1.45,3.6,d/2-1.45,P.WHITE);
  for(let i=0;i<4;i++)g.push().tf(w/2-6,.3,-14+i*1.8),sheetStack(g,0,0,2.6,1.4,.8+(i%2)*.5,i%2?P.WHITE:P.CHROME),g.pop();
  g.pop();}

/* ===== Sheet stock and shipping platform ===== */
KIT('pvc_stock',{
  label:{es:'Expediciones',en:'Stock & shipping',pt:'Expedição',fr:'Stock et expéditions'},
  desc:'Sheet stock and shipping platform: a cut-away warehouse (no roof, no south wall) with racks of sheet bundles, forklifts and a glass shipping office, loading docks with box trucks, a yard of bundles and two flatbeds loaded with bundles ready to leave. Good for building-materials logistics, finished-goods stock, order preparation and export shipping.',
  origin:[-1718,-10],box:[-1800,-80,-1630,50],flat:[[-1718,-10,160]],gate:[-1660,48],water:null,
  icon:'<path d="M5 4h14v16H5zM5 9.3h14M5 14.7h14"/>',
  shot:{t:[-1720,0,-20],W:84,H:70,az:36,el:31,fov:30,sx:.25},
  anchors:{warehouse:[-1725,14,-22],docks:[-1678,6,-26],yard:[-1680,4,12],forklifts:[-1725,4,-22],office:[-1699,4.2,-9],depart:[-1650,5,-58],loading:[-1650,5,-40],label:[-1725,40,-22],arc:[-1725,14,-22]},
  signs:{plant:{slot:'T_X1',text:{es:'EXPEDICIONES',en:'SHIPPING',pt:'EXPEDIÇÃO',fr:'STOCK ET EXPÉDITIONS'},band:'BY'}},
  build(g,K){
    slab(g,rectPoly(-1790,-72,-1640,36,6));road(g,[[-1660,48],[-1660,-60]],8,.27);road(g,[[-1690,-6],[-1660,-6]],7,.27);
    on(g,.25,()=>{sheetWarehouse(g,-1725,-22,K.sign('plant'));
      for(const z of[-34,-26.5,-19])truckStatic(g,-1679.15,z,0,[P.BR,P.WHITE,P.BR][(z|0)%3===0?1:0],mkBoxTrailer);
      for(let i=0;i<4;i++)for(let j=0;j<2;j++)sheetStack(g,-1681.2+i*3,10+j*2.8,2.6,2.2,.9+((i+j)%3)*.35,[P.WHITE,P.CHROME,P.FB][(i+j)%3]);
      flatbedStatic(g,-1650,-58,-Math.PI/2,P.WHITE,P.WHITE);flatbedStatic(g,-1650,-40,-Math.PI/2,P.BR,P.CHROME);});
    for(let x=-1778;x<-1640;x+=10)if(Math.abs(x+1660)>7)tree(g,x,41,.95,(x/10|0)%3===0?1:0,x|0);
    HARD(g,[[-1699,-18],[-1738,-28]],.55);
    K.dyn.walk.push({route:K.walk([-1745,-14],[-1706,-14],1.3,3),cloth:P.CLOTH,vest:P.VEST,helmet:P.HELMET,y:.55});
    K.dyn.fork.push({route:K.fork([-1748,-25.5],[-1702,-25.5]),y:.55,load:true},{route:K.fork([-1745,-18.5],[-1706,-18.5]),y:.55,load:false},{route:K.fork([-1686,4],[-1686,-15],2.5),y:.25,load:true});}
});

/* ===== PVC sheet plant: extrusion & bi-orientation ===== */
KIT('pvc_plant',{
  label:{es:'Fábrica',en:'Plant',pt:'Fábrica',fr:'Usine'},
  desc:'Sheet extrusion plant (PVC, plastics, building materials): a ribbed production hall with translucent roof strips that opens on the close-up onto two extrusion and bi-orientation lines (extruders with hoppers, die and calender rolls, stretching oven, forming rolls, cutter and stacker, operators and a forklift); resin silos with a pipe bridge and a bulk tanker; a cooling unit and basin; an R&D and pilot-line building; a transformation workshop; a control room and a quality lab that open; a stockyard of sheet bundles under a canopy with forklifts; trucks loading; offices that open onto the sales-admin and service desks; parking.',
  origin:[0,-20],box:[-150,-110,150,70],flat:[[0,-20,230]],gate:[30,84],water:null,lamps:true,keep:[[22,56,38,90]],
  icon:'<path d="M3 21V10l5 3V10l5 3V6h3v15M16 9h5v12M2 21h20"/>',
  shot:{t:[0,0,-30],W:150,H:110,az:36,el:32,fov:30,sx:.24,dmin:96},
  anchors:{hall:[-15,18,-65],line:[4,4.5,-66],silos:[-95,21,-78],cooling:[58,8,-73],rd:[103,10,-68],control:[43,6,-32],lab:[38,5,-10],crew:[8,4,-36],
    transfo:[92,11,-21],stock:[-96,10,-27],loading:[-30,4,28],offices:[103,10,17],adv:[92,3.6,12],meeting:[113,3.6,22],direction:[118,3.6,8],parking:[64,3,19],label:[0,48,-50],arc:[-15,26,-65]},
  pads:{hall:6},
  signs:{plant:{slot:'T_DOCK',text:{es:'PLANTA',en:'PLANT',pt:'FÁBRICA',fr:'USINE'},band:'BY'},
         office:{slot:'T_TERM',text:{es:'OFICINAS',en:'OFFICES',pt:'ESCRITÓRIOS',fr:'BUREAUX'},band:'BY'}},
  build(g,K){
    slab(g,rectPoly(-140,-100,140,58,8),.25,P.PAVE2);
    road(g,[[-128,46],[128,46],[128,-92],[-128,-92],[-128,46]],7);road(g,[[30,84],[30,46]],9);
    g.flat(rectPoly(-122,33,122,43,2),.27,P.PAVE);
    on(g,.25,()=>{
      /* production hall: north and west walls stay; south and east walls, the roof (translucent strips), band, sign and logo open */
      g.rbox(-50,0,-84,20,.12,-46,.04,P.CONC,P.PAVE2);g.box(-50,0,-84,20,14,-83.6,P.STEEL,P.MID);g.box(-50,0,-84,-49.6,14,-46,P.STEEL,P.MID);
      const hc=K.cut('hall',['hall','line','crew'],g);
      hc.box(-50,0,-46.4,20,14,-46,P.STEEL,P.MID);for(let x=-48;x<20;x+=4)hc.box(x,0,-46.02,x+.4,14,-45.86,P.LIGHT);
      hc.box(19.6,0,-84,20,14,-46.4,P.STEEL,P.MID);for(let z=-82;z<-46;z+=4)hc.box(20,0,z,20.14,14,z+.4,P.LIGHT);
      hc.box(-50.2,0,-46.3,20.2,2.2,-45.8,P.CONC);for(const x of[-34,-2])hc.box(x,0,-45.84,x+7,6.5,-45.76,P.DARK);
      hc.gable(-50.4,-84.4,20.4,-45.6,14,2.4,P.MID,P.STEEL,true);
      const th=Math.atan2(2.4,19.4);for(const s of[-1,1])for(let x=-46;x<18;x+=8){hc.push().tf(x+1.2,15.22,-65+s*9.7);hc.rx(s*th);hc.box(-1.1,0,-7.4,1.1,.08,7.4,P.WHITE,P.WHITE);hc.pop();}
      hc.box(-50.1,9.4,-46,20.1,12.8,-45.74,P.BY);
      hc.decal([-6,11.1,-45.7],[1,0,0],[0,1,0],20,2.5,[0,0,1],K.sign('plant'),P.BY);hc.decal([-38,11.1,-45.7],[1,0,0],[0,1,0],9,3,[0,0,1],UV.LOGOW,P.BY);
      extrusionLine(g,-46,16,-72);extrusionLine(g,-46,16,-60);
      for(const[x,z,a]of[[-38,-66,0],[-14,-55.6,Math.PI],[6,-66,0],[-26,-77.4,0]])personStatic(g,x,z,a,P.CLOTH2,-1,P.VEST);
      for(let k=0;k<4;k++)sheetStack(g,-44+k*3.2,-50.2,2.6,2.4,.9+(k%2)*.5,k%2?P.WHITE:P.CHROME);
      /* resin silos, pipe bridge, bulk tanker */
      for(const[x,z]of[[-110,-82],[-101,-82],[-92,-82],[-83,-82],[-105.5,-72],[-96.5,-72],[-87.5,-72]])silo(g,x,z,3.4,15);
      g.box(-114,15,-83,-79,15.6,-71,P.STEEL);g.tube([-80,15.8,-77],[-50,11.5,-72],.45,8,P.STEEL);g.tube([-80,15.8,-75],[-50,11.5,-70],.35,8,P.STEEL);
      for(const u of[.2,.6]){const x=-80+30*u,y=15.8-4.3*u,zc=-76+3*u;g.box(x-.3,0,zc-1.6,x+.3,y-.5,zc-1,P.STEEL);g.box(x-.3,0,zc+1,x+.3,y-.5,zc+1.6,P.STEEL);g.box(x-.3,y-.6,zc-1.6,x+.3,y-.4,zc+1.6,P.STEEL);}
      truckStatic(g,-90,-60,0,P.WHITE,gg=>mkTrailer(gg,P.MID,P.LIGHT,P.TANK));
      /* cooling unit on a steel table, cooling-water basin */
      for(const x of[46,54,62,70])for(const z of[-75.6,-70.4])g.box(x-.25,0,z-.25,x+.25,5,z+.25,P.STEEL);airCooler(g,58,-73,26,5);g.cyl(36,-73,0,4.4,2.2,24,P.CONC,P.WATER2);
      /* R&D centre and pilot line */
      office(g,84,-82,122,-56,9,P.BR,UV.OFFICE);winLights(g,84,-82,122,-56,9,'sw');g.rbox(86,9,-80,96,10.4,-74,.1,P.MID,P.LIGHT);
      /* transformation workshop (special parts, cut-to-size) */
      g.rbox(64,0,-32,120,9,-10,.2,P.STEEL,P.MID);for(let x=66;x<120;x+=4)g.box(x,0,-9.98,x+.4,9,-9.84,P.LIGHT);g.box(63.9,6.2,-9.9,120.1,7.4,-9.7,P.BR);
      for(let x=70;x<118;x+=9){g.push().tf(x,9.04,-21);g.box(-1.6,0,-9,1.6,.08,9,P.WHITE,P.WHITE);g.pop();}for(const x of[76,100])g.box(x,0,-9.86,x+6,6,-9.78,P.DARK);
      /* control room and quality lab: both open on the close-up */
      openBuilding(g,K.cut('control',['control','crew','lab','hall','line'],g),30,-40,56,-24,7,{band:P.BR,tex:UV.WARM,fill:g=>{const Rr=rng(41);videoWall(g,32.4,53.6,-39.6,1.4,3.4);consoleArc(g,43,-40,8,5,Rr);
        personStatic(g,52,-27,2.6,P.CLOTH2);}});
      openBuilding(g,K.cut('lab',['lab','control','crew','line'],g),28,-17,50,-4,5,{band:P.BY,tex:UV.OFFICE,lights:true,fill:g=>{for(const z of[-14.5,-9])g.rbox(31,0,z,47,1,z+1.6,.06,P.WHITE,P.LIGHT);
        for(const[x,z]of[[33,-14.2],[39.5,-8.7]])g.rbox(x,1,z,x+1.3,1.75,z+1,.05,P.MID,P.SCREEN);g.rbox(43,1,-14.4,46.4,2.3,-13,.06,P.DARK,P.LW);
        for(let k=0;k<5;k++)g.box(31.4+k*.5,1,-8.9,31.5+k*.5,2.4,-7.6,k%2?P.WHITE:P.CHROME);personStatic(g,36,-11.6,1.2,P.WHITE);personStatic(g,44,-11.8,3.4,P.WHITE);}});
      permitTent(g,8,-37.5,0);personStatic(g,4,-35.4,.5,P.CLOTH,P.HELMET,P.VEST);personStatic(g,12.2,-34.6,2.8,P.CLOTH2,P.HELMET,P.VEST);
      /* stockyard: a canopy over bundles, open-air rows, loading bay */
      for(const x of[-122,-112,-102,-92,-82])for(const z of[-42,-14])g.box(x-.3,0,z-.3,x+.3,8,z+.3,P.STEEL);g.rbox(-123,8,-43,-81,8.5,-13,.1,P.MID,P.LIGHT);
      const C3=[P.WHITE,P.CHROME,P.FB,P.WHITE],C4=[P.CHROME,P.WHITE,P.CA];
      for(let x=-120;x<-84;x+=4.6)for(let z=-39;z<-16;z+=3.6)sheetStack(g,x,z,3.4,2.4,1+(((x*7+z)|0)&3)*.35,C3[((x+z)|0)&3]);
      for(let x=-76;x<-58;x+=4.6)for(let z=-38;z<-14;z+=3.6)sheetStack(g,x,z,3.4,2.4,.8+(((x+z*3)|0)&3)*.3,C4[((((x-z)|0)%3)+3)%3]);
      for(let k=0;k<4;k++)sheetStack(g,-40+k*3.6,25.6,3,2.4,1.1,k%2?P.WHITE:P.CHROME);
      /* offices: sales administration and customer service (they open on the close-up) */
      const oc=K.cut('offices',['offices','adv','meeting','direction','parking'],g);
      openBuilding(g,oc,84,4,122,30,8,{band:P.BR,tex:UV.OFFICE,lights:true,fill:g=>{const Rr=rng(23);for(let i=0;i<4;i++)for(const z of[10,17])deskPod(g,90+i*6.2,z,3,Rr);
        meetTable(g,113,22,5,2.4,Rr);videoWall(g,108,118,4.4,2.2,2.4);desk(g,118.4,8.6,0,P.CLOTH2);for(const[x,z,a]of[[96,24,2.4],[110,12,-1],[116,25.6,.6]])personStatic(g,x,z,a,P.CLOTH2);
        for(const[x,z]of[[85,5],[121,5],[121,29],[85,29]])pottedPlant(g,x,z,1);}});
      oc.rbox(83.7,8,29.9,122.3,9.5,30.5,.06,P.BY,P.BY);oc.decal([108,8.75,30.56],[1,0,0],[0,1,0],11.2,1.4,[0,0,1],K.sign('office'),P.BY);oc.decal([91,8.75,30.56],[1,0,0],[0,1,0],4.2,1.4,[0,0,1],UV.LOGOW,P.BY);
      parkingLot(g,48,8,80,30,6,.7);});
    fence(g,[[-146,62],[22,62]]);fence(g,[[38,62],[146,62],[146,-106]]);
    for(let x=-140;x<142;x+=10){if(x>18&&x<42)continue;tree(g,x,68+(Math.abs(x)%2),1,(x/10|0)%3===0?1:0,x|0);}
    const rA=K.route([[-114,41],[114,41],[114,36],[-114,36]],8,[{x:-30,z:36,d:9}],2.5);
    K.dyn.trucks.push({route:rA,off:0,cab:P.BY,trailer:'box'},{route:rA,off:.5,cab:P.WHITE,trailer:'box'});
    K.dyn.walk.push({route:K.walk([-40,-43],[24,-43],1.1,5),cloth:P.CLOTH,vest:P.VEST,y:.27},{route:K.walk([86,1.5],[120,1.5],1.2,4),cloth:P.CB,y:.27});
    K.dyn.fork.push({route:K.fork([-78,-8],[-44,20]),y:.25,load:true},{route:K.fork([-44,-53],[12,-53],2.5),y:.25,load:true},{route:K.fork([-118,-10],[-86,-10]),y:.25,load:false});}
});

/* ===== Builders' merchant + DIY store ===== */
KIT('negoce',{
  label:{es:'Distribución',en:'Merchants & DIY',pt:'Revendas',fr:'Négoces et GSB'},
  desc:'Where building products are sold: a DIY big-box store whose facade and roof open on the close-up (aisles, a display of roofing sheets, shoppers and a department manager), a garden-centre greenhouse, a builders\' merchant with a sales counter that opens (staff, a contractor, a technical sales rep), an open-front materials shed with cantilever racks, a yard of sheet bundles with forklifts and a delivery truck, the rep\'s branded car and a big parking lot. Good for building materials, hardware, distribution networks, trade counters and DIY retail.',
  origin:[0,0],box:[-104,-60,104,46],flat:[[0,-6,140]],gate:[60,60],water:null,lamps:true,keep:[[54,36,66,64]],
  icon:'<path d="M3 10l2-6h14l2 6M4 10v10h16V10M3 10h18M9 20v-5h6v5"/>',
  shot:{t:[-6,0,-16],W:120,H:94,az:28,el:31,fov:30,sx:.24},
  anchors:{gsb:[-49,13,-40],rayon:[-34,3.6,-29],garden:[-87,7,-42],comptoir:[-1,4.6,-46],hangar:[48,10,-43],yard:[24,4,-17],rep:[8,3.4,-29],parking:[-50,3,8],label:[-10,34,-30],arc:[-49,15,-40]},
  signs:{gsb:{slot:'T_LUB',text:{es:'BRICOLAJE',en:'DIY STORE',pt:'CONSTRUÇÃO',fr:'BRICOLAGE'},band:'BR'},
         negoce:{slot:'T_CARG',text:{es:'MATERIALES',en:'BUILDERS MERCHANT',pt:'MATERIAIS',fr:'NÉGOCE MATÉRIAUX'},band:'BR'}},
  build(g,K){slab(g,rectPoly(-100,-58,100,42,5));road(g,[[60,60],[60,34]],8,.27);
    on(g,.25,()=>{
      /* DIY store: north and west walls stay; south and east walls, roof and fascia open */
      g.rbox(-72,0,-56,-26,.12,-24,.04,P.CONC,P.PAVE2);g.box(-72,0,-56,-26,9,-55.6,P.WHITE,P.LIGHT);g.box(-72,0,-56,-71.6,9,-24,P.WHITE,P.LIGHT);
      const sc=K.cut('gsb',['gsb','rayon'],g);
      sc.box(-72,0,-24.4,-26,9,-24,P.WHITE,P.LIGHT);sc.box(-26.4,0,-56,-26,9,-24.4,P.WHITE,P.LIGHT);sc.rbox(-72.3,9,-56.3,-25.7,9.6,-23.7,.08,P.LIGHT,P.LIGHT);
      sc.box(-56,0,-23.96,-44,4.2,-23.84,P.GLASS);sc.box(-72.2,6.4,-23.9,-25.8,8.8,-23.66,P.BR);sc.decal([-44,7.6,-23.6],[1,0,0],[0,1,0],16,2,[0,0,1],K.sign('gsb'),P.BR);
      sc.rbox(-58,4.2,-23.9,-42,4.6,-21.6,.06,P.WHITE,P.LIGHT);
      for(let k=0;k<6;k++){const z=-52+k*4.4;g.box(-69,0,z-.5,-40,2.4,z+.5,P.LIGHT);g.decal([-54.5,1.25,z+.52],[1,0,0],[0,1,0],28,2,[0,0,1],UV.SHELF,P.LIGHT);}
      /* roofing-sheet display near the entrance: sheets leaning on a rack */
      g.rbox(-38,0,-34,-29,.3,-30.6,.04,P.MID,P.MID);g.box(-38,0,-34.2,-29,3.2,-33.9,P.DARK);
      for(let k=0;k<8;k++){const x=-37.4+k*1.1;g.push().tf(x,0,-32.4);g.rx(-.2);g.box(-.48,.3,-.04,.48,3.1,.04,[P.WHITE,P.CHROME,P.FB,P.CA][k%4]);g.pop();}
      for(const[x,z,a,c]of[[-33,-28.6,Math.PI,P.CB],[-31.2,-29.2,-2.4,P.BR],[-50,-36.6,1,P.CD],[-60,-45.6,0,P.CLOTH2]])personStatic(g,x,z,a,c);
      /* garden centre greenhouse */
      greenhouse(g,null,-98,-54,-76,-30,4.2,7.3);for(let x=-96;x<-77;x+=2.4)g.box(x,0,-52,x+1.2,1,-32,P.TREE);
      /* builders' merchant: sales counter (opens), materials shed, yard */
      const ct=K.cut('comptoir',['comptoir','rep'],g);
      openBuilding(g,ct,-14,-56,12,-38,5.5,{band:P.BR,tex:UV.OFFICE,fill:g=>{g.rbox(-10,0,-47,8,1.1,-45.8,.06,P.WOOD,P.WOOD);for(const x of[-6,2])g.rbox(x,1.1,-46.9,x+1.2,1.7,-46.1,.04,P.DARK,P.SCREEN);
        for(const[x,z,a,c]of[[-5,-48.6,0,P.CLOTH2],[3,-48.6,0,P.CLOTH2],[-2,-43.4,Math.PI,P.VEST],[5.6,-42.6,-2.6,P.CLOTH]])personStatic(g,x,z,a,c);
        for(let k=0;k<4;k++)g.box(-12.6,0,-54+k*2.6,-11.2,2.2,-52.4+k*2.6,P.LIGHT);}});
      ct.rbox(-14.3,4.6,-37.95,12.3,6.1,-37.4,.06,P.BR,P.BR);ct.decal([-1,5.35,-37.34],[1,0,0],[0,1,0],12,1.5,[0,0,1],K.sign('negoce'),P.BR);
      g.box(18,0,-56,78,8,-55.6,P.STEEL,P.MID);for(let x=18;x<=78;x+=10)g.box(x-.3,0,-33.3,x+.3,8,-32.7,P.STEEL);g.box(18,0,-56,18.4,8,-33,P.STEEL,P.MID);
      g.rbox(17.6,8,-56.4,78.4,8.5,-32.6,.08,P.MID,P.LIGHT);for(let x=22;x<76;x+=8){g.push().tf(x,8.52,-44.5);g.box(-1,0,-11.6,1,.06,11.6,P.WHITE,P.WHITE);g.pop();}
      for(let x=22;x<76;x+=6){g.box(x-.15,0,-54,x+.15,6,-53.6,P.RACK);for(let y=1.2;y<6;y+=1.6)g.box(x-.12,y,-53.6,x+.12,y+.12,-50,P.RACK);}
      const C5=[P.WHITE,P.WOOD,P.CHROME,P.MID],C6=[P.WHITE,P.CHROME,P.FB],C7=[P.WHITE,P.CHROME,P.WOOD,P.CA];
      for(let x=21;x<77;x+=2.6)for(let y=1.32;y<6;y+=1.6)g.box(x,y,-53.4,x+2.3,y+.3+((((x*3+y*7)|0)%3+3)%3)*.1,-50.4,C5[((x+y)|0)%4]);
      for(let x=24;x<74;x+=5.2)sheetStack(g,x,-40,4,2.4,.9+((x|0)%3)*.3,C6[((x/5.2)|0)%3]);
      for(let x=4;x<92;x+=5)for(const z of[-22,-12])if(x<34||x>48)sheetStack(g,x,z,3.6,2.4,.8+(((x+z)|0)&3)*.3,C7[((x/5|0)+(z<-15?1:0))%4]);
      flatbedStatic(g,84,10,Math.PI,P.WHITE,P.WHITE);
      /* the technical sales rep's branded car at the counter */
      g.push().tf(8,0,-31.6,0);carLow(g,0,0,0,P.WHITE);g.decal([0,.75,.9],[1,0,0],[0,1,0],1.6,.53,[0,0,1],UV.LOGOW,P.WHITE);g.pop();personStatic(g,12.4,-34,-2.4,P.CLOTH2);
      parkingLot(g,-96,-16,-8,30,12,.72);for(const x of[-80,-40,0,40,80])lampPost(g,x,39,7,Math.PI/2);});
    for(let x=-100;x<104;x+=12)if(Math.abs(x-60)>8)tree(g,x,42+(Math.abs(x)%2),.85,(x/12|0)%3===0?1:0,x|0);
    K.dyn.walk.push({route:K.walk([-70,-20],[-28,-20],1.2,4),cloth:P.CB,y:.27},{route:K.walk([-20,-31],[-20,-18],1.1,5),cloth:P.CD,y:.27});
    K.dyn.fork.push({route:K.fork([40,-28],[40,6]),y:.25,load:true},{route:K.fork([20,-30],[76,-30],2.4),y:.25,load:false});
    const lp=K.route([[58,60],[58,34],[-4,34],[-4,30],[62,30],[62,60]],6,[{x:10,z:34,d:8}],3);K.dyn.cars.push({route:lp,off:0,col:P.CB,kind:2},{route:lp,off:.5,col:P.CC,kind:0});}
});

/* ===== Roofing site: a farm or industrial building being roofed ===== */
KIT('chantier',{
  label:{es:'Obra',en:'Job site',pt:'Obra',fr:'Chantier'},
  desc:'Construction site of a steel-frame farm or industrial building: portal frames and purlins, half of the roof already clad with corrugated sheets and translucent strips, roofers at work on the roof, scaffolding along the eaves, a truck crane lifting a bundle of sheets, a flatbed delivery with bundles on the gravel, a forklift, site cabins with the site sign, and a technical sales rep with a tablet beside the branded car, talking with the site manager. Good for roofing, cladding, installation and specification stages.',
  origin:[0,0],box:[-72,-50,72,32],flat:[[0,-10,112]],gate:[50,48],water:null,lamps:false,keep:[[44,28,56,52]],
  icon:'<path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6M2 10l10-7 10 7"/>',
  shot:{t:[-8,0,-14],W:92,H:72,az:30,el:30,fov:30,sx:.24},
  anchors:{roof:[-22,12.5,-28],roofers:[-7,10.5,-20],crane:[34,16,-24],delivery:[30,5.5,4],stock:[30,4,-6],rep:[-3,4,15],hut:[-30,7,7],scaffold:[-26,6,-12],label:[-10,32,-26],arc:[-22,13,-28]},
  pads:{roofers:28},
  signs:{site:{slot:'T_X6',text:{es:'OBRA',en:'JOB SITE',pt:'OBRA',fr:'CHANTIER'},band:'WHITE'}},
  build(g,K){slab(g,rectPoly(-68,-46,68,28,4),.25,P.SAND);road(g,[[50,48],[50,24]],7,.27);g.flat(rectPoly(26,-2,60,24,2),.27,P.PAVE);
    on(g,.25,()=>{
      /* steel frames, purlins, plinth and north cladding */
      for(let x=-40;x<=20;x+=6)for(const z of[-42,-14])g.box(x-.25,0,z-.25,x+.25,7,z+.25,P.STEEL);
      for(let x=-40;x<=20;x+=6){g.tube([x,7,-42],[x,9.5,-28],.2,4,P.STEEL,P.STEEL,false);g.tube([x,7,-14],[x,9.5,-28],.2,4,P.STEEL,P.STEEL,false);}
      for(let k=0;k<=6;k++){const u=k/6;for(const zs of[-42,-14]){const z=zs+(-28-zs)*u,y=7+2.5*u;g.tube([-40,y+.12,z],[20,y+.12,z],.07,4,P.STEEL,P.STEEL,false);}}
      g.box(-40,0,-42.3,20,7,-41.9,P.LIGHT,P.MID);g.box(-40.3,0,-42,-39.9,7,-14,P.LIGHT,P.MID);g.box(-40,0,-14.2,20,1.6,-13.8,P.CONC);
      /* the clad part of the roof: corrugated sheets with translucent strips */
      const th=Math.atan2(2.5,14),L=Math.hypot(14,2.5);
      for(const s of[-1,1]){g.push().tf(-22,8.42,-28+s*7);g.rx(s*th);g.box(-18,0,-L/2,18,.08,L/2,P.MID,P.LIGHT);
        for(let x=-17.6;x<18;x+=.8)g.box(x,.08,-L/2,x+.22,.14,L/2,P.LIGHT);for(const x of[-15,-9,-3,3,9,15])g.box(x-.55,.15,-L/2,x+.55,.18,L/2,P.WHITE,P.WHITE);g.pop();}
      /* roofers on the south slope, one carrying a sheet */
      for(const[x,z,a]of[[-6.4,-20,1.4],[-8.6,-24.5,-.4],[-5.2,-26.4,2.2]]){const y=9.5-2.5*(z+28)/14;g.push().tf(0,y+.3,0);personStatic(g,x,z,a,P.CLOTH,P.HELMET,P.VEST);g.pop();}
      g.push().tf(-7.6,8.7,-22);g.rx(th);g.box(-.5,1.1,-1.8,.5,1.16,1.8,P.WHITE);g.pop();
      scaffold(g,-40,-13.6,-6,-11.6,7);
      /* crane lifting a bundle over the bare frames */
      truckCrane(g,36,-24,Math.PI,32,.86);
      /* delivery and stock on the gravel */
      flatbedStatic(g,40,6,Math.PI,P.WHITE,P.WHITE);for(let k=0;k<5;k++)sheetStack(g,24+(k%3)*4.2,-8+(k/3|0)*3.4,3.6,2.4,.9+(k%2)*.4,k%2?P.WHITE:P.CHROME);
      /* site cabins, site sign, the rep and the site manager */
      g.rbox(-36,0,4,-24,2.8,10,.08,P.WHITE,P.LIGHT);g.rbox(-36,2.8,4,-24,5.6,10,.08,P.WHITE,P.LIGHT);
      for(const y of[1,3.8])for(const x of[-34,-31,-28])g.box(x,y,10.02,x+1.6,y+1,10.08,P.GLASS);for(const y of[0,2.8])g.box(-25.6,y,10.02,-24.6,y+2.2,10.08,P.DARK);
      g.box(-26.2,2.7,10.1,-24,2.9,11.6,P.STEEL);for(let y=.3;y<2.7;y+=.48)g.box(-23.9,y,10.6,-23.4,y+.1,11.2,P.STEEL);g.box(-23.9,0,10.5,-23.8,2.8,10.6,P.STEEL);
      for(const x of[34,41.6])g.box(x-.1,0,19.9,x+.1,3.4,20.1,P.STEEL);g.box(33.6,2.1,20.1,42,3.3,20.3,P.WHITE);g.decal([37.8,2.7,20.34],[1,0,0],[0,1,0],8,1,[0,0,1],K.sign('site'),P.WHITE);
      g.push().tf(-8,0,12,0);carLow(g,0,0,0,P.WHITE);g.decal([0,.75,.9],[1,0,0],[0,1,0],1.6,.53,[0,0,1],UV.LOGOW,P.WHITE);g.pop();
      personStatic(g,-3.6,14.6,-2.2,P.CLOTH2);g.box(-3.3,1.15,14.2,-2.9,1.5,14.4,P.SCREEN);personStatic(g,-2,13.2,.9,P.CLOTH,P.HELMET,P.VEST);
      for(let k=0;k<6;k++)cone(g,30+k*2.4,-16.5);});
    fence(g,[[-66,26],[44,26]]);fence(g,[[56,26],[66,26],[66,-44],[-66,-44],[-66,26]]);
    for(let x=-64;x<66;x+=11)if(Math.abs(x-50)>9)tree(g,x,30.5,.85,(x/11|0)%2,x|0);
    K.dyn.walk.push({route:K.walk([-21,8],[-19,-9],1.1,5),cloth:P.CLOTH,vest:P.VEST,helmet:P.HELMET,y:.25});
    K.dyn.fork.push({route:K.fork([44,-2],[38,-12],2.5),y:.25,load:true});}
});

/* ===== Farm with greenhouses and a livestock building (PV on the roof) ===== */
KIT('agri_serres',{
  label:{es:'Agro',en:'Farms & greenhouses',pt:'Agro',fr:'Agriculture et serres'},
  desc:'Farm customer: a multi-span greenhouse whose roof and facades open on the close-up (crop rows, a grower), a livestock building with open sides, cows inside, a translucent ridge and roof strips, the south slope covered with solar panels and installers finishing it from a scaffold tower, three silos, a farmhouse and a crop field with a tractor. Good for agriculture, greenhouse growers, farm buildings and rooftop solar stages.',
  origin:[0,0],box:[-84,-66,84,48],flat:[[0,-10,132]],gate:[56,64],water:null,lamps:false,keep:[[50,44,62,68]],
  icon:'<path d="M3 20V11l4.5-5L12 11l4.5-5L21 11v9M3 20h18M7.5 6v14M16.5 6v14"/>',
  shot:{t:[-12,0,-30],W:118,H:90,az:30,el:31,fov:30,sx:.24},
  anchors:{serre:[-51,9.5,-37],cultures:[-44,3.2,-30],barn:[24,13,-43],herd:[6,3.6,-37],cour:[46,3.5,-19],pv:[16,10.5,-35],installer:[46,10,-35],scaffold:[57,6,-30],silos:[68,16,-48],house:[38,7,8],field:[-28,3,24],label:[-10,32,-36],arc:[-51,11,-37]},
  pads:{herd:24,pv:22},
  signs:{},
  build(g,K){
    g.strip([[56,64],[56,-24]],4.5,.06,P.SAND);g.flat(rectPoly(-6,-26,80,-16,2),.05,P.SAND);g.strip([[-22,-14],[-22,-6],[56,-6]],4,.07,P.SAND);
    on(g,0,()=>{
      /* greenhouse: crop rows inside, a grower and a trolley */
      g.flat(rectPoly(-78,-58,-24,-16,1),.06,P.PAVE2);
      greenhouse(g,K.cut('serre',['serre','cultures','field'],g),-78,-58,-24,-16,4.4,9);
      for(let x=-76.4;x<-25;x+=1.9)g.rbox(x,.06,-56,x+.8,1.3+((((x*5)|0)%3+3)%3)*.12,-24,.1,P.TREE2,P.TREE);
      g.box(-78,.06,-22,-24,.09,-18.4,P.CONC);personStatic(g,-44,-21,2.6,P.CLOTH2);g.rbox(-41,.1,-21.6,-39,1,-20.4,.05,P.STEEL,P.LIGHT);personStatic(g,-61.75,-26.4,.4,P.CB);
      /* livestock building: open sides, cows, translucent ridge and strips; PV on the south slope */
      g.rbox(-6,0,-58,54,.2,-28,.05,P.CONC,P.SAND);
      for(let x=-6;x<=54;x+=6)for(const z of[-58,-28])g.box(x-.2,0,z-.2,x+.2,5,z+.2,P.WOOD);
      g.box(-6,0,-58.2,54,1.4,-57.8,P.CONC);g.box(-6,2.6,-58.2,54,5,-57.9,P.WOOD);g.box(-6,0,-28.2,54,1.4,-27.8,P.CONC);g.box(-6.2,0,-58,-5.8,1.4,-28,P.CONC);g.box(53.8,0,-58,54.2,1.4,-28,P.CONC);
      const th=Math.atan2(4,15),L=Math.hypot(15,4);
      for(const s of[-1,1]){g.push().tf(24,7.08,-43+s*7.5);g.rx(s*th);g.box(-30.5,0,-L/2,30.5,.12,L/2,P.MID,P.LIGHT);
        if(s<0)for(let x=-27;x<30;x+=6)g.box(x-.6,.12,-L/2+.6,x+.6,.16,L/2-.6,P.WHITE,P.WHITE);g.pop();}
      g.box(-6.5,8.96,-43.7,54.5,9.24,-42.3,P.WHITE,P.WHITE);
      g.push().tf(24,7.08,-35.5);g.rx(th);for(let x=-28.6;x<14;x+=2.12)for(let zz=-6.6;zz<6.8;zz+=1.7)g.box(x,.14,zz,x+2,.22,zz+1.6,P.GLASS,P.GLASS);
      for(let zz=-6.6;zz<6.8;zz+=1.7)g.box(14.2,.14,zz,16.2,.22,zz+1.6,P.GLASS,P.GLASS);g.pop();
      for(let i=0;i<14;i++){const x=-2+(i%7)*7.6,z=i<7?-33:-50;cow(g,x,.2,z,i<7?Math.PI/2+(i%3-1)*.3:-Math.PI/2+(i%2)*.4,i%3?P.COW:P.COW2);}
      g.box(-5,.2,-41.2,53,1,-40.6,P.CONC);
      /* installers on the roof and their scaffold tower */
      for(const[x,z,a]of[[44,-36.4,1.6],[48,-33.4,-1.2]]){const y=9-4*(z+43)/15;g.push().tf(0,y+.25,0);personStatic(g,x,z,a,P.CLOTH,P.HELMET,P.VEST);g.pop();}
      scaffold(g,55,-34,59,-29,5.2);for(let k=0;k<3;k++)g.rbox(61,0,-30+k*2.4,63.2,.9,-28.4+k*2.4,.04,P.GLASS,P.GLASS);
      /* silos, farmhouse, field and tractor */
      silo(g,66,-54,3.2,12);silo(g,74,-46,3.2,12);silo(g,66,-38,2.6,10);
      house(g,38,8,11,8.5,4.2,2.8,P.WHITE,P.ROOF,0);
      field(g,rectPoly(-80,2,22,42,2),P.FA,P.FB,3.2,0);});
    for(const[x,z]of[[28,16],[46,17],[-4,-12],[70,10],[72,-20]])tree(g,x,z,1,(x+z)&1,x*7+z|0);
    const rows=[];for(let k=0;k<4;k++){const z=8+k*9;rows.push(k%2?[16,z]:[-74,z]);rows.push(k%2?[-74,z]:[16,z]);}
    K.dyn.veh.push({mesh:'ftractor',route:new Route(K.path(rows,4,true),3.8),fw:1.2,rad:4});
    K.dyn.walk.push({route:K.walk([-2,-22],[50,-22],1.0,6),cloth:P.CLOTH2,y:.06});}
});
