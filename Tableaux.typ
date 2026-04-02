#let etat_1 = json("ETATS.json").at(0)
#let etat_2 = json("ETATS.json").at(1)
#let etat_3 = json("ETATS.json").at(2)
#let etat_4 = json("ETATS.json").at(3)

#align(center)[
  #table(
    columns: 3,
    [*Configuration*], [*Cisaillement max*], [*Normale max*],
    ["Configuration 1"], [#etat_1], [#etat_1],
    ["Configuration 2"], [#etat_2], [#etat_2],
    ["Configuration 3"], [#etat_3], [#etat_3],
    ["Configuration 4"], [#etat_4], [#etat_4],

  )
]
