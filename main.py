from flask import Flask, render_template
import requests

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def index():
  r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false')  
  coin = r.json()
  return render_template('index.html', len = len(coin), coin = coin)
  
# https://api.coinbase.com/v2/prices/BTC-USD/spot
@app.route('/crypto/<id>')
def crypto(id):
   r = requests.get('https://api.coinbase.com/v2/prices/'+ id  +'/spot')
   return r.json()


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
