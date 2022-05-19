#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import datetime
from flask import *  # pip install flask
import random as rd
from datetime import timedelta

from flask import sessions

app = Flask(__name__)
app.secret_key = str(rd.randint(0, 9999999999999999999999999))

def getEmail():
    if 'email_user' in session:
        return session['email_user']
    else:
        return "Invité(e)"

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)

@app.route("/")
def hello():
    db = sqlite3.connect('static/DATABASE/wesh.db')
    cur = db.cursor()
    
    data_tendances_home = ""

    for row in cur.execute("SELECT * FROM Produits WHERE Review > 4.5 LIMIT 10"):
        id_product = str(row[0])
        prix = "{:,.2f}".format(row[1]).replace(",", "").replace(".", ",")
        titre = str(row[2])
        desc = str(row[3])
        image = str(row[4]).split(";")[0]
        percent = str(round(row[5] * 100 / 5))
        
        data_tendances_home += """<li>
                        <a class="card shadow h-100" href='/product?id=""" + id_product + """'>
                            <div class="ratio ratio-1x1 parent">
                                <img src='""" + image + """' class="card-img-top child" loading="lazy" alt="...">
                            </div>
                            <div class="card-body d-flex flex-column flex-md-row">
                                <div class="flex-grow-1">
                                    <strong>""" + titre + """</strong>
                                    <p class="card-text">""" + desc + """</p>
                                </div>
                                <div class="px-md-2">""" + prix + """€</div>
                            </div>
                            <strong><p style="color: rgb(230, 73, 0);margin: 0px 20px 20px 20px;">🔥 """ + percent + """% des utilisateurs ont aimé cet article.</p></strong>
                        </a>
                    </li>"""
    
    data_promo_home = ""
    for row in cur.execute("SELECT * FROM Produits WHERE DATE(PromoDate) > DATE('" + str(datetime.datetime.now()) + "') LIMIT 10"):
        id_product = str(row[0])
        prix = "{:,.2f}".format(row[1]).replace(",", "").replace(".", ",")
        titre = str(row[2])
        desc = str(row[3])
        image = str(row[4]).split(";")[0]
        promo_prix = ""
        if (row[7] != None) : promo_prix = "{:,.2f}".format(row[7]).replace(",", "").replace(".", ",")
        data_promo_home += """<li>
                    <a class="card shadow h-100" href='/product?id=""" + id_product + """'>
                        <div class="ratio ratio-1x1 parent">
                            <img src='""" + image + """' class="card-img-top child" loading="lazy" alt="...">
                        </div>
                        <div class="card-body d-flex flex-column flex-md-row">
                            <div class="flex-grow-1">
                                <strong>""" + titre + """</strong>
                                <p class="card-text">""" + desc + """</p>
                            </div>
                            <div class="px-md-2">
                                <p style="text-decoration: line-through; margin: 0px;">""" + prix + """€</p>
                                <strong><p style="color: white; background-color: rgb(255, 0, 0);margin: 0px"> """ + promo_prix + """€ </p></strong>
                            </div>
                        </div>
                    </a>
                </li>"""

    data_reco_home = ""
    for row in cur.execute("SELECT * FROM Produits WHERE Type == 'Ordinateurs' or Type == 'Electroniques' LIMIT 10"):
        id_product = str(row[0])
        prix = "{:,.2f}".format(row[1]).replace(",", "").replace(".", ",")
        titre = str(row[2])
        desc = str(row[3])
        image = str(row[4]).split(";")[0]
            
        data_reco_home += """<li>
                    <a class="card shadow h-100" href='/product?id=""" + id_product + """'>
                        <div class="ratio ratio-1x1 parent">
                            <img src='""" + image + """' class="card-img-top child" loading="lazy" alt="...">
                        </div>
                        <div class="card-body d-flex flex-column flex-md-row">
                            <div class="flex-grow-1">
                                <strong>""" + titre + """</strong>
                                <p class="card-text">""" + desc + """</p>
                            </div>
                            <div class="px-md-2">""" + prix + """€</div>
                        </div>
                    </a>
                </li>"""
    db.close()
    return render_template("home.html", html_recommendations = Markup(data_reco_home), html_promos = Markup(data_promo_home), html_topventes = Markup(data_tendances_home), email = getEmail())
@app.route("/login", methods=['POST', 'GET'])
def login():
    message = ""
    password = request.form.get('password')
    email = request.form.get('email')
    if (password != None and email != None):
        db = sqlite3.connect('static/DATABASE/wesh.db')
        cur = db.cursor()
        for row in cur.execute("SELECT * FROM Utilisateurs WHERE Password = '" + password + "' AND Email = '" + email + "'"):
            if row[2] == 0:
                session['admin_pass'] = True
                session['email_user'] = email
                db.close()
                return """<script>document.location.href="/admin";</script>""", 301
            else:
                session['email_user'] = email
                db.close()
                return """<script>document.location.href="/";</script>""", 301
        message = "<p style='color: red'>Le mot de passe et/ou l'e-mail est incorrecte !</p>"
        db.close()
    return render_template("login.html", html_message = Markup(message))

@app.route("/product")
def product():
    id_product = request.args.get("id")
    db = sqlite3.connect('static/DATABASE/wesh.db')
    cur = db.cursor()
    row = cur.execute("SELECT * FROM Produits WHERE Id == " + str(id_product)).fetchone()
    if row == None: abort(404)
    prix = row[1]
    titre = str(row[2])
    desc = str(row[3])
    images_1 = ""
    images_2 = ""
    counter = 1
    for url in str(row[4]).split(";"):
        if counter == 1:
            images_1 += """<label id='little_image""" + str(counter) + """' class="thumb gallery_show_little_img" style="background-image: url('""" + str(url) + """')" onclick="ShowImage('""" + str(counter) + """')"></label>"""
            images_2 += """<figure id='big_image""" + str(counter) + """' class="gallery_show_big_img"><label for="fullscreen"><img src='""" + str(url) + """'></label></figure>"""
        else:
            images_1 += """<label id='little_image""" + str(counter) + """' class="thumb" style="background-image: url('""" + str(url) + """')" onclick="ShowImage('""" + str(counter) + """')"></label>"""
            images_2 += """<figure id='big_image""" + str(counter) + """' class=""><label for="fullscreen"><img src='""" + str(url) + """'></label></figure>"""
        counter+=1
    note = str(row[5])
    promo_date = str(row[6])
    promo_prix = row[7]
    if promo_prix != None and promo_prix != '':
        promo_prix = "<div style='text-decoration: line-through;font-weight: 400;'>" + "{:,.2f}".format(prix).replace(",", "").replace(".", ",") + " €</div><div style='colorcolor=white;color: white;background-color: red;font-weight: 600;padding: 4px;margin-right: 10px;'>-" + str(round(((prix - promo_prix) / prix) * 100)) + " %</div>"
        prix = "<div style='colorcolor=white;color: red;font-weight: 1000;'>" + "{:,.2f}".format(row[7]).replace(",", "").replace(".", ",") + " €</div>"
    else:
        promo_prix = ""
        prix = "{:,.2f}".format(prix).replace(",", "").replace(".", ",") + " €"
    prix_livraison = row[8]
    if prix_livraison == None or prix_livraison == '':
        prix_livraison = "Gratuit !"
    else:
        prix_livraison = "{:,.2f}".format(prix_livraison).replace(",", "").replace(".", ",") + " €"
    caracteritiques = ""
    if str(row[9]) != "None" and str(row[9]) != "":
        for cara in str(row[9]).split('\n'):
            caracteritiques += "<tr><td>" + cara.split(";")[0] + "</td><td>" + cara.split(";")[1] + "</td></tr>"
    type_ = str(row[10])
    db.close()

    return render_template("product.html", prix_produit = Markup(prix), titre_produit = titre, description_produit = desc, images_produit_1 = Markup(images_1), images_produit_2 = Markup(images_2), promo_prix_produit = Markup(promo_prix), type_produit = type_, note_produit = note, caracteritiques_produit = Markup(caracteritiques), promo_date_produit = promo_date, prix_livraison_produit = prix_livraison, email = getEmail())
@app.route("/promos")
def promos():
    db = sqlite3.connect('static/DATABASE/wesh.db')
    cur = db.cursor()
    data_promo = ""
    for row in cur.execute("SELECT * FROM Produits WHERE DATE(PromoDate) > DATE('" + str(datetime.datetime.now()) + "')"):
        id_product = str(row[0])
        prix = "{:,.2f}".format(row[1]).replace(",", "").replace(".", ",")
        titre = str(row[2])
        desc = str(row[3])
        image = str(row[4]).split(";")[0]
        promo_prix = ""
        if (row[7] != None) : promo_prix = "{:,.2f}".format(row[7]).replace(",", "").replace(".", ",")
        data_promo += """<div class="gallery">
                <a class="card shadow h-100" href='/product?id=""" + id_product + """'>
                    <div class="ratio ratio-1x1">
                        <img src='""" + image + """' class="card-img-top" loading="lazy" alt="...">
                    </div>
                    <div class="card-body d-flex flex-column flex-md-row">
                        <div class="flex-grow-1">
                            <strong>""" + titre + """</strong>
                            <p class="card-text">""" + desc + """</p>
                        </div>
                        <div class="px-md-2">
                            <p style="text-decoration: line-through; margin: 0px;">""" + prix + """€</p>
                            <strong><p style="color: white; background-color: rgb(255, 0, 0);margin: 0px"> """ + promo_prix + """€ </p></strong>
                        </div>
                    </div>
                </a>
            </div>"""
    db.close()
    return render_template("promos.html", html_produit = Markup(data_promo), email = getEmail())
@app.route("/rechercher")
def rechercher():
    db = sqlite3.connect('static/DATABASE/wesh.db')
    cur = db.cursor()
    data = ""
    for row in cur.execute("SELECT * FROM Produits"):
        id_product = str(row[0])
        prix = "{:,.2f}".format(row[1]).replace(",", "").replace(".", ",")
        titre = str(row[2])
        desc = str(row[3])
        image = str(row[4]).split(";")[0]
        data += """<div class="gallery produits" search-data=" """ + titre + " " + desc + """ ">
                <a class="card shadow h-100" href='/product?id=""" + id_product + """'>
                    <div class="ratio ratio-1x1">
                        <img src='""" + image + """' class="card-img-top" loading="lazy" alt="...">
                    </div>
                    <div class="card-body d-flex flex-column flex-md-row">
                        <div class="flex-grow-1">
                            <strong>""" + titre + """</strong>
                            <p class="card-text">""" + desc + """</p>
                        </div>
                        <div class="px-md-2">
                            <p style="margin: 0px;">""" + prix + """€</p>
                        </div>
                    </div>
                </a>
            </div>"""
    db.close()
    return render_template("rechercher.html", html_produit = Markup(data), email = getEmail())
@app.route("/admin", methods=['POST', 'GET'])
def admin():
    if 'admin_pass' in session:
        db = sqlite3.connect('static/DATABASE/wesh.db')
        cur = db.cursor()

        message = ""
        id_ = request.form.get('id_prod')
        price = request.form.get('Prix')
        title = request.form.get('Titre')
        desc = request.form.get('Description')
        imgs = request.form.get('Images')
        revw = request.form.get('Avis')
        promo_date = request.form.get('PromoDate')
        promo_price = request.form.get('PromoPrice')
        deliv_price = request.form.get('DeliveryPrice')
        tech_info = request.form.get('TechnicalInfo')
        type_ = request.form.get('Type')
        if id_ != None:
            # delete item by id
            try:
                cur.execute("""DELETE FROM Produits WHERE Id = """ + id_)
                db.commit()
                message = """<div class="alert-success">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <strong>Succès !</strong> Le produit à bien été supprimé.</div>"""
            except sqlite3.OperationalError as msg:
                message = """<div class="alert-err">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <strong>Erreur !</strong> """ + str(msg) + """</div>"""
        elif price != None and title != None and desc != None and imgs != None and tech_info != None and type_ != None:
            # add item with post info
            try:
                if promo_price != '': price = float(price)
                if deliv_price != '': deliv_price = float(deliv_price)


                vals = str((float(price), title, desc, imgs, float(revw), promo_date, promo_price, deliv_price, tech_info, type_)).replace("\\r\\n", """
""")
                cur.execute("INSERT INTO Produits(Id,Price,Title,Description,Images,Review,PromoDate,PromoPrice,DeliveryPrice,TechnicalInfo,Type) VALUES(NULL," + vals[1:])
                db.commit()
                message = """<div class="alert-success">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <strong>Succès !</strong> Le produit à bien été ajouté.</div>"""
            except sqlite3.OperationalError as msg:
                message = """<div class="alert-err">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <strong>Erreur !</strong> """ + str(msg) + """</div>"""
        data = ""
        for row in cur.execute("SELECT * FROM Produits"):
            id_product = str(row[0])
            titre = str(row[2])
            data += "<option value=" + str(id_product) + ">" + titre + "</option>"
        db.close()
        return render_template("admin.html", html_options_produits = Markup(data), html_message = Markup(message))
    else:
        return abort(401)
@app.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")

@app.errorhandler(401)
def access_denied(e):
    return render_template('error.html', titre = "Erreur 401 : Accès refusé", message = "La page que vous cherchez est protégé par une authentification. Veuillez d'abord vous connecter."), 401

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', titre = "Erreur 404 : Page introuvable", message = "La page que vous cherchez n'existe pas/plus."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', titre = "Erreur 500 : Erreur interne", message = "Aïe... Il semblerait qu'une erreur critique se soit produite, vous avez casser le serveur :'("), 500


# -------------- Ne pas modifier ↓ --------------
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=35000)
