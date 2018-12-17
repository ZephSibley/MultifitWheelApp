from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from tables import base, Make, Model, config, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_


app = Flask(__name__)

base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


# Routing
@app.route('/')
def index():
    provided_parameters = {}
    session = DBSession()

    make_table = session.query(Make).all()
    MakeSelection = request.args.get("MakeSelection", None)
    provided_parameters["MakeSelection"] = MakeSelection
    myfilteredmodels = session.query(Model)
    if MakeSelection is not None:
        myfilteredmodels = myfilteredmodels.filter(Model.makeid==MakeSelection)

    ModelSelection = request.args.get("ModelSelection", None)
    provided_parameters["ModelSelection"] = ModelSelection
    myfilteredyears = session.query(config.Year)
    if ModelSelection is not None:
        myfilteredyears = myfilteredyears.filter(config.modelid==ModelSelection)

    YearSelection = request.args.get("YearSelection", None)
    provided_parameters["YearSelection"] = YearSelection

    result = []
    if provided_parameters["MakeSelection"] and provided_parameters["ModelSelection"] and provided_parameters["YearSelection"]:
        result = session.query(config).filter(and_(config.makeid == provided_parameters["MakeSelection"], config.modelid == provided_parameters["ModelSelection"], config.Year == provided_parameters["YearSelection"])).all()


    return render_template('home.html', makes=make_table, models=myfilteredmodels, years=myfilteredyears, provided_parameters=provided_parameters, result=result)
