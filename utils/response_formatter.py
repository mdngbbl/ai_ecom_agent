import matplotlib.pyplot as plt
import io
import base64

def plot_bar_chart(data: list, x_key: str, y_key: str):
    x = [item[x_key] for item in data]
    y = [item[y_key] for item in data]
    plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(f"{y_key} by {x_key}")
    plt.xticks(rotation=45)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
