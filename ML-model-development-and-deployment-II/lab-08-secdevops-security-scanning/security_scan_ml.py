import pandas as pd

# Sample scan data
data = {
    "severity": [
        "high","medium","low",
        "high","medium","low",
        "high","medium","low"
    ],

    "vulnerability_type":[
        "SQL Injection",
        "Cross-site Scripting",
        "Information Disclosure",
        "SQL Injection",
        "Cross-site Scripting",
        "Cross-site Scripting",
        "SQL Injection",
        "SQL Injection",
        "Information Disclosure"
    ],

    "score":[
        9.8,7.2,4.5,
        9.3,6.8,3.5,
        9.9,8.0,4.2
    ]
}

df = pd.DataFrame(data)

severity_map = {
    "low":0,
    "medium":1,
    "high":2
}

df["severity"] = df["severity"].map(severity_map)

print(df)
