 #Begin the method to calculate ionionization energies for various atoms and electronic states
 +from pyne import nucname
  import numpy as np
  def function(element,charge):
  	#initialize tuples 
 +	#parse input
 +	index = nucname.znum(element)
  	#element tuples
 -	element = (null,null,He, Li ,Be ,B ,C ,N ,O ,F ,Ne ,Na ,Mg ,Al ,Si ,P ,S ,Cl ,Ar ,K ,Ca ,Sc ,Ti,V ,Cr,Mn,Fe ,Co ,Ni ,Cu ,Zn ,Ga ,Ge ,As ,Se ,Br ,Kr ,Rb ,Sr ,Y ,Zr ,Mo ,Tc ,Ru ,Rh ,Pd ,Ag ,Cd ,In ,Sn ,Sb ,Te ,I ,Xe ,Cs ,Ba ,La ,Ce ,Pr ,Nd ,Pm ,Sm ,Eu ,Gd ,Tb ,Dy ,Ho ,Er ,Tm ,Yb ,Lu ,Hf ,Ta ,W ,Re ,Os ,Ir ,Pt ,Au ,Hg ,Tl ,Pb ,Bi ,Po ,At ,Rn ,Fr ,Ra ,Ac ,Th ,Pa,U,Np,Pu,Am,Cm ,Bk,Cf,Es)
 +	elements = (null,null,He, Li ,Be ,B ,C ,N ,O ,F ,Ne ,Na ,Mg ,Al ,Si ,P ,S ,Cl ,Ar ,K ,Ca ,Sc ,Ti,V ,Cr,Mn,Fe ,Co ,Ni ,Cu ,Zn ,Ga ,Ge ,As ,Se ,Br ,Kr ,Rb ,Sr ,Y ,Zr ,Mo ,Tc ,Ru ,Rh ,Pd ,Ag ,Cd ,In ,Sn ,Sb ,Te ,I ,Xe ,Cs ,Ba ,La ,Ce ,Pr ,Nd ,Pm ,Sm ,Eu ,Gd ,Tb ,Dy ,Ho ,Er ,Tm ,Yb ,Lu ,Hf ,Ta ,W ,Re ,Os ,Ir ,Pt ,Au ,Hg ,Tl ,Pb ,Bi ,Po ,At ,Rn ,Fr ,Ra ,Ac ,Th ,Pa,U,Np,Pu,Am,Cm ,Bk,Cf,Es)
  	#individual tuples
  	He = [null]
  	Li = [null]
 @@ -106,4 +109,5 @@ def function(element,charge):
  	#GO BEARS!!!!
  	Cf = [null]
  	Es = [null]
 +	return elements[index][charge]
  	pass