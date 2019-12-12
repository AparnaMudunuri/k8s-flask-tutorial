from flask import Flask,render_template,request,redirect,url_for

#import config

app = Flask(__name__)

url_dict = {
    'none':'https://www.royallifemart.com/img/product-not-found.jpg',
    'jacket' :'data:image/jpeg;base64,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',
    'ring': 'https://lh3.googleusercontent.com/no4sswlB5vAdizoIBSOxXHDpwXbGfYyKWT66EGANHSm614Uf-HGdPWzK-WijW02tH7scLw=s100',
    'scarf':'https://lh3.googleusercontent.com/OW6Rlg_2-ggek9lx6GViZbf9nIaDVPsYzOcEu8Dcmh-_yjMo4fpiBprJNjJ0U0QP_S2vcy4=s96',
    'shirt':'https://images-na.ssl-images-amazon.com/images/I/41xCWDx-OyL.jpg',
    'shoes':'data:image/jpeg;base64,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'
        }

app.route('/')
def show_first():
    return render_template("index.html")

@app.route('/show_index/<select_key>')
def show_index(select_key):
    return render_template("index.html", user_image = url_dict[select_key])


@app.route('/',methods=['POST','GET'])
def my_form_post():
    select_key = 'none'
    text = request.form['u']
    url_key = text.lower()
    
    for each in url_dict:
        if url_key in each:
            select_key = each
            break
    
    return redirect(url_for('show_index',select_key=select_key))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
