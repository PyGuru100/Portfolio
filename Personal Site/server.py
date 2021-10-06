from flask import Flask, render_template, send_file

app = Flask(__name__)
software_dict = {'img_name': 'programmer',
                 'job_title': 'Software Developer',
                 'special_tile': 'Github',
                 'css': 'software',
                 'special_link': 'https://github.com/PyGuru100/projects',
                 'resume': 'software/resume'}
chem_dict = {'img_name': 'chem',
             'job_title': 'Chemical Engineer',
             'special_tile': 'Projects',
             'css': 'chem',
             'resume': 'chem/resume'}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/software')
def software():
    return render_template('softchem.html', vars_dict=software_dict)


@app.route('/chem')
def chem():
    return render_template('softchem.html', vars_dict=chem_dict)


@app.route('/chem/resume')
def chem_resume():
    return send_file('static/chem.png')


@app.route('/software/resume')
def soft_resume():
    return send_file('static/programmer.png')


if __name__ == '__main__':
    app.run(debug=True)
