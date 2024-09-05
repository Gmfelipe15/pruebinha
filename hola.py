from flask import Flask, render_template, request, redirect, session,  url_for, flash

@app.route('/hola')
def hola():
  return render_template('hola.html')

   
if __name__ =='__main__':
   app.run(debug=True)