#let etat_1 = json("ETATS.json").at("1")
#let etat_2 = json("ETATS.json").at("2")
#let etat_3 = json("ETATS.json").at("3")
#let etat_4 = json("ETATS.json").at("4")
#let etat_5 = json("ETATS.json").at("5")
#let Petit_Tunnel = json("ETATS.json").at("Petit tunnel")


#align(center)[
  #table(
    columns: 5, 
    [*Configuration*], [*Cisaillement max (MPa)*], [*Facteur de sécurité en cisaillement*], [*Normale max (MPa)*], [*Facteur sécurité en compresison*],
    [*Configuration 1*], [#etat_1.at(0).at(0)], [#etat_1.at(0).at(1)], [#etat_1.at(1).at(0)], [#etat_1.at(1).at(1)],
    [*Configuration 2*], [#etat_2.at(0).at(0)], [#etat_2.at(0).at(1)], [#etat_2.at(1).at(0)], [#etat_2.at(1).at(1)],
    [*Configuration 3*], [#etat_3.at(0).at(0)], [#etat_3.at(0).at(1)], [#etat_3.at(1).at(0)], [#etat_3.at(1).at(1)],
    [*Configuration 4*], [#etat_4.at(0).at(0)], [#etat_4.at(0).at(1)], [#etat_4.at(1).at(0)], [#etat_4.at(1).at(1)],
    [*Configuration 5*], [#etat_5.at(0).at(0)], [#etat_5.at(0).at(1)], [#etat_5.at(1).at(0)], [#etat_5.at(1).at(1)],
    [*Petit tunnel*], [0], [-], [#Petit_Tunnel.at(0)], [#Petit_Tunnel.at(1)]
  )
]





