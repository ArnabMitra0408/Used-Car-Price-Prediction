import joblib
from src.utils.code_files.common_utils import read_params
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)
print("starting acquiring params")
configs=read_params('params.yaml')
print("params acquired")
def file_load(path:str,type:str='pkl'):
    file=joblib.load(path)
    return file

ml_model = file_load(configs['model_training']['best_model'])
scaler_x=file_load(configs['model_training']['scaler_x'])
scaler_y=file_load(configs['model_training']['scaler_y'])


body_type=file_load(configs['pickle_files']['body_type_encoding'])
brake_type=file_load(configs['pickle_files']['brake_type_encoding'])
brand=file_load(configs['pickle_files']['brand_encoding'])
car_seller_type=file_load(configs['pickle_files']['seller_type_encoding'])
drive_type=file_load(configs['pickle_files']['drive_type_encoding'])
fuel_type=file_load(configs['pickle_files']['fuel_type_encoding'])
gear_type=file_load(configs['pickle_files']['gear_box_encoding'])
model_type=file_load(configs['pickle_files']['model_encoding'])
owner_type=file_load(configs['pickle_files']['owner_type_encoding'])
state=file_load(configs['pickle_files']['state_encoding'])
steering_type=file_load(configs['pickle_files']['steering_type_encoding'])
transmission_type=file_load(configs['pickle_files']['transmission_type_encoding'])
tyre_type=file_load(configs['pickle_files']['tyre_type_encoding'])


inputs=[]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        brand_name=brand.transform([request.form["Brand_Name"]])[0]
        inputs.append(int(brand_name))

        model_name=model_type.transform([request.form["Model_Name"]])[0]
        inputs.append(int(model_name))

        state_name=state.transform([request.form["state"]])[0]
        inputs.append(int(state_name))
        
        inputs.append(int(request.form["Manufactured_Year"]))

        owner=owner_type.transform([request.form["owner_type"]])[0]
        inputs.append(int(owner))

        body_name=body_type.transform([request.form["body_type"]])[0]
        inputs.append(int(body_name))

        transmission_name=transmission_type.transform([request.form["Transmission_Type"]])[0]
        inputs.append(int(transmission_name))

        inputs.append(int(request.form["Insurance_Premium"]))

        fuel_name=fuel_type.transform([request.form["fuel_type"]])[0]
        inputs.append(int(fuel_name))

        inputs.append(float(request.form["KM_Driven"]))

        car_seller=car_seller_type.transform([request.form["Car_Seller_Type"]])[0]
        inputs.append(int(car_seller))

        inputs.append(float(request.form["Displacement"]))
        
        inputs.append(int(request.form["Num_Cylinder"]))

        inputs.append(int(request.form["Valves_Per_Cylinder"]))

        inputs.append(int(request.form["Turbo_Charger"]))

        inputs.append(int(request.form["Super_Charger"]))

        inputs.append(float(request.form["length"]))
        
        inputs.append(float(request.form["Wheel_Base"]))

        inputs.append(float(request.form["Front_Tread"]))

        gear=gear_type.transform([request.form["gear_type"]])[0]
        inputs.append(int(gear))

        drive=drive_type.transform([request.form["drive_type"]])[0]
        inputs.append(int(drive))

        inputs.append(float(request.form["Seating_Capacity"]))

        steering=steering_type.transform([request.form["steering_type"]])[0]
        inputs.append(int(steering))

        front_brake=brake_type.transform([request.form["front_brake_type"]])[0]
        inputs.append(int(front_brake))

        rear_brake=brake_type.transform([request.form["rear_brake_type"]])[0]
        inputs.append(int(rear_brake))

        inputs.append(float(request.form["Acceleration"]))

        tyre=tyre_type.transform([request.form["tyre_type"]])[0]
        inputs.append(int(tyre))

        inputs.append(int(request.form["Num_Doors"]))

        inputs.append(float(request.form["mileage"]))

        inputs.append(float(request.form["Alloy_Wheel_Size"]))

        inputs.append(float(request.form["Max_Power_Delivered"]))

        inputs.append(float(request.form["Max_Power_At"]))

        para=np.array(inputs)
        para=para.reshape(1,-1)
        price=ml_model.predict(para)[0]
    return render_template("index.html",car_price=price)

if __name__ == "__main__":

    app.run(debug=True)