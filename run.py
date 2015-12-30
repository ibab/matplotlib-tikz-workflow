
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pgf_with_custom_preamble = {
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
    "pgf.texsystem": "lualatex",
    "pgf.preamble": [
         "\\usepackage{tikz}",
         "\\usepackage{unicode-math}",
         "\\tikzstyle{every picture}+=[remember picture]",
         "\\tikzstyle{na} = [baseline=-.5ex]",
         ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

plt.figure(figsize=(4, 3))

x = np.linspace(0, 1, 200)

plt.plot(x, x**2, 'b-')
plt.text(0.5, 0.8, r'\tikz[na] \coordinate (plot); Text')
plt.savefig('out.pgf')

