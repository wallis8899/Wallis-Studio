from flask import Flask, render_template,request
from DataBase import Video, db, session, engine

app = Flask(__name__)
@app.route("/")
def index():
	#for p in session.query(Video):

	return render_template("devs.html", vid=session.query(Video))


@app.route("/Admin", methods=["POST","GET"])
def admin():
	if request.method == 'POST':
		url = request.form.get("url")
		title = request.form.get("title")
		desc = request.form.get("desc")
		if url and title and desc != "":
			try:
				data_send = Video(Url=url,Title=title,Desc=desc)
				session.add(data_send)
				session.commit()
				session.close()
			except Exception:
				session.merge(data_send)
				session.close()

		else:
			pass
	return render_template("admin.html")



app.run(host=44.227.217.144", port=80)

