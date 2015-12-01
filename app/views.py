from app import app, loader
from forms import InputForm
from flask import render_template, flash, redirect, url_for, request
# from sets import Set

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	# tags = []
	tags = set()
	empty = 1
	if form.validate_on_submit():
		for description in form.desList:
			fData = description.data['des']
			if fData and fData != 'None' and fData not in tags:
					empty = 0
					# tags.append(fData)
					tags.add(fData)
		if not empty:
			title, TagDic, score = ComputeMatch(tags)
			return render_template('index.html', results=[title, TagDic, score], form=form)
	return render_template('index.html', form=form)


def ComputeMatch(tags):

	score = 0
	title = ""
	for k, v in loader.items():
		cur_score = 0
		intersection = []
		union = []
		v_set = set(v)
		intersection = list(tags & v_set)
		union = list(tags | v_set)
		cur_score = float(len(intersection))/len(union)
		if cur_score > score:
			score = cur_score
			title = k
			# print (intersection, union)

	print(title, loader[title], score)	
	return title, loader[title], score







