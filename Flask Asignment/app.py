from flask import Flask, request, render_template_string

app = Flask(__name__)

main_page = '''
<html>
    <head>
    <title>Multiplier</title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<legend>Multiplier</legend>
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>  
  <div class="col-md-4">
  <input id="textinput" type="number" name='number' placeholder="Enter a number" class="form-control input-md">
  </div>
</div>
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>
</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(main_page)

@app.route('/calc', methods=['POST'])
def calc():
    number = request.form.get('number', type=int)
    result = number * 5
    return f'The result of {number} multiplied by 5 is: {result}'

if __name__ == '__main__':
    app.run(debug=True)
