import pandas as pd

# Direct Arylation Settings
substances = {
    "solvents": {
        "DMAc": r"CC(N(C)C)=O",
        "Butyornitrile": r"CCCC#N",
        "Butyl Ester": r"CCCCOC(C)=O",
        "p-Xylene": r"CC1=CC=C(C)C=C1",
    },
    "bases": {
        "Potassium acetate": r"O=C([O-])C.[K+]",
        "Potassium pivalate": r"O=C([O-])C(C)(C)C.[K+]",
        "Cesium acetate": r"O=C([O-])C.[Cs+]",
        "Cesium pivalate": r"O=C([O-])C(C)(C)C.[Cs+]",
    },
    "ligands": {
        "BrettPhos": r"CC(C)C1=CC(C(C)C)=C(C(C(C)C)=C1)C2=C(P(C3CCCCC3)C4CCCCC4)C(OC)="
        "CC=C2OC",
        "Di-tert-butylphenylphosphine": r"CC(C)(C)P(C1=CC=CC=C1)C(C)(C)C",
        "(t-Bu)PhCPhos": r"CN(C)C1=CC=CC(N(C)C)=C1C2=CC=CC=C2P(C(C)(C)C)C3=CC=CC=C3",
        "Tricyclohexylphosphine": r"P(C1CCCCC1)(C2CCCCC2)C3CCCCC3",
        "PPh3": r"P(C1=CC=CC=C1)(C2=CC=CC=C2)C3=CC=CC=C3",
        "XPhos": r"CC(C1=C(C2=CC=CC=C2P(C3CCCCC3)C4CCCCC4)C(C(C)C)=CC(C(C)C)=C1)C",
        "P(2-furyl)3": r"P(C1=CC=CO1)(C2=CC=CO2)C3=CC=CO3",
        "Methyldiphenylphosphine": r"CP(C1=CC=CC=C1)C2=CC=CC=C2",
        "1268824-69-6": r"CC(OC1=C(P(C2CCCCC2)C3CCCCC3)C(OC(C)C)=CC=C1)C",
        "JackiePhos": r"FC(F)(F)C1=CC(P(C2=C(C3=C(C(C)C)C=C(C(C)C)C=C3C(C)C)C(OC)=CC=C2OC)"
        r"C4=CC(C(F)(F)F)=CC(C(F)(F)F)=C4)=CC(C(F)(F)F)=C1",
        "SCHEMBL15068049": r"C[C@]1(O2)O[C@](C[C@]2(C)P3C4=CC=CC=C4)(C)O[C@]3(C)C1",
        "Me2PPh": r"CP(C)C1=CC=CC=C1",
    },
}
temperatures = [90, 105, 120]
concentrations = [0.057, 0.1, 0.153]
lookup = pd.read_csv("../data/direct_arylation.csv")
