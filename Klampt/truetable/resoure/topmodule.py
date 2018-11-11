import sys
import time

with open ('./logicVerilog/prm_lgcchk_top.v','w') as vFile:
	vFile.write('module prm_lgcchk_top\n(\ninput A,\ninput B,\ninput C,\ninput D,\ninput E,\ninput F,\ninput G,\ninput H,\ninput I,\ninput J,\ninput K,\ninput L,\ninput M,\ninput N,\ninput O,\noutput [1023:0] edge_mask\n);\n')

	for k in range(0,1024):	
		vFile.write('prm_oblgc_chk'+str(k)+' i_prm_oblgc_chk'+str(k)+'(\n')
		vFile.write('.A(A),\n.B(B),\n.C(C),\n.D(D),\n.E(E),\n.F(F),\n.G(G),\n.H(H),\n')
		vFile.write('.I(I),\n.J(J),\n.K(K),\n.L(L),\n.M(M),\n.N(N),\n.O(O),\n.edge_mask(edge_mask['+str(k)+'])\n);\n')

			


	vFile.write('endmodule')


			

				#vFile.write(data)
