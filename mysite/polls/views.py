import numpy as np
from scipy.integrate import solve_ivp
import yfinance as yf
import matplotlib.pyplot as plt

def black_scholes(t, y):
    S, V = y
    dSdt = r * S + sigma * S * np.random.normal(0, 1)
    dVdt = 0.5 * sigma ** 2 * S ** 2 * V - r * V
    return [dSdt, dVdt]

r = 0.05
sigma = 0.2

msft = yf.Ticker("MSFT")
S0 = msft.history(period="1d")["Close"][0]
V0 = 0.04

sol = solve_ivp(black_scholes, [0, 1], [S0, V0])

print(sol.y)

plt.plot(sol.t, sol.y[0])
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.show()
