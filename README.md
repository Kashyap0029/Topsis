# Topsis

---

## ⚙️ Methodology (TOPSIS Steps)

1. Normalize the decision matrix  
2. Apply weights to the normalized matrix  
3. Determine ideal best and ideal worst solutions  
4. Compute distance from ideal best and worst  
5. Calculate TOPSIS score  
6. Rank alternatives based on scores  

---

## ✅ Result Table

The output table includes:
- Original criteria values  
- **TOPSIS Score** for each alternative  
- **Rank** (1 = best alternative)

Example result:

| Fund | Topsis Score | Rank |
|----|-------------|------|
| M3 | 0.861481 | 1 |
| M7 | 0.695464 | 2 |
| M4 | 0.588547 | 3 |
| M2 | 0.468008 | 4 |
| M5 | 0.450754 | 5 |
| M8 | 0.414151 | 6 |
| M6 | 0.326624 | 7 |
| M1 | 0.215165 | 8 |

✔ Higher TOPSIS score indicates a better alternative.

---

## 📊 Result Graph

A bar chart is generated to compare TOPSIS scores across alternatives.

- **X-axis:** Alternatives (M1, M2, …)  
- **Y-axis:** TOPSIS Score  
- Helps in quick visual comparison  
- Confirms ranking obtained from the table  

Example visualization:
