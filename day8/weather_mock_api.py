from flask import Flask,request,jsonify, Response
import random

app = Flask(__name__)

@app.route("/weather/<city>")
def city(city):
    formatt = request.args.get("format",'json')
    temp = random.randint(20,40)
    
    if formatt == 'xml':
        data = f"""
        <weather>
            <city>{city}</city>
            <temparature>{temp}</temparature>
            <format>xml</format>
        </weather>
        """
        return Response(data, content_type='application/xml')
    
    
    return jsonify(dict(city=city,temparature=temp,format='json'))
    
if __name__ == '__main__':
    app.run()