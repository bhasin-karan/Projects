//Referenced https://www.geeksforgeeks.org/working-with-forms-using-express-js-in-node-js/ and https://www.npmjs.com/package/python-shell
// and https://blog.postman.com/understanding-async-await-in-node-js/
const express = require('express');
const app = express();
var bodyParser = require('body-parser');
let { PythonShell } = require('python-shell');

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.get('/', function(req, res) {
    res.render('form');
});

app.post('/submit-form', async function(req, res) {

    console.log('User information', req.body);

    const { age, sex, weight, heightFeet, heightInches, physicalActivity, familyHistoryCancer, familyHistoryHeartDisease } = req.body;

    //Convert sex to binary
    let sexNumeric;
    if (sex==='Male'){
        sexNumeric = 1;
    } else {sexNumeric = 0}

    //Calculate BMI (Formula from: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html)
    const weightInPounds = weight;
    const heightInInches = parseInt(heightFeet) * 12 + parseInt(heightInches);
    const bmi = ((weightInPounds / (heightInInches**2))*703).toFixed(2);

    //Adding categories
    let bmiText = ""
    if (bmi < 18.5){
        bmiText = `${bmi} - Underweight`
    } else if (bmi < 25){
        bmiText = `${bmi} - Healthy`
    } else if (bmi < 30){
        bmiText = `${bmi} - Overweight`
    } else if (bmi > 30){
        bmiText = `${bmi} - Obese`
    }

    ageEntered = parseInt(age);
    //Converting user age to age group to pass as Age Parameter for Cancer Dashboard URL
    let ageGroupCancer = ""
    lowRangeSubtrahend = ageEntered%5;
    if (ageEntered > 84){
        ageGroupCancer = "85+ years";
    } else if (ageEntered === 0){
        ageGroupCancer = "< 1 year";
    } else{
        if (ageEntered <= 4){
        lowRange = ageEntered - lowRangeSubtrahend  + 1;
        upperRange = lowRange + 3;
    } else {
        lowRange = ageEntered - lowRangeSubtrahend;
        upperRange = lowRange + 4;
    }
    lowRangeString = lowRange.toString();
    upperRangeString = upperRange.toString();
    ageGroupCancer = `${lowRangeString}-${upperRangeString} years`
    }

    //Converting user age to age group to pass as Age Parameter for Heart Disease Dashboard URL
    let ageGroupHeart = ""
    if (ageEntered < 45){
        ageGroupHeart = "18–44 years";
    } else if (ageEntered >= 45 && ageEntered < 55){
        ageGroupHeart = "45–54 years";
    } else if (ageEntered >= 55 && ageEntered < 65){
        ageGroupHeart = "55–64 years";
    } else if (ageEntered >= 65 && ageEntered < 75){
        ageGroupHeart = "65–74 years";
    } else if (ageEntered >= 75){
        ageGroupHeart = "75 years and over";
    }

    let optionsForCancer = {
        mode: 'text',
        pythonOptions: ['-u'],
        args: [age, bmi, sexNumeric, physicalActivity, familyHistoryCancer]
        };

    let optionsForHeartDisease = {
            mode: 'text',
            pythonOptions: ['-u'],
            args: [age, bmi, sexNumeric, physicalActivity, familyHistoryHeartDisease]
        };

    try {
        //Calculating Cancer and Heart Disease Risk Scores
        let cancerResults = await PythonShell.run('RiskScoreCalc/cancer_risk_score.py', optionsForCancer);
        let heartDiseaseResults = await PythonShell.run('RiskScoreCalc/heart_risk_score.py', optionsForHeartDisease);
        console.log('Cancer Risk', cancerResults);
        console.log('Heart Disease Risk', heartDiseaseResults);

        const cancerRisk = cancerResults[0];
        const heartDiseaseRisk = heartDiseaseResults[0];
        const tableauCancerDashboardUrl = `https://public.tableau.com/views/CancerOccurrenceDashboard/CancersDashboard?:embed=y&:showVizHome=no&Age%20Parameter=${encodeURIComponent(ageGroupCancer)}&Sex%20Parameter=${encodeURIComponent(sex)}&Race%20Parameter=${encodeURIComponent(req.body.race)}`;
        const tableauHeartDashboardUrl = `https://public.tableau.com/views/HeartDiseasePercentDashboard/HeartDiseaseDashboard?:embed=y&:showVizHome=no&Age%20Parameter=${encodeURIComponent(ageGroupHeart)}&Sex%20Parameter=${encodeURIComponent(sex)}`;

        console.log('Results', cancerRisk, heartDiseaseRisk, tableauCancerDashboardUrl, tableauHeartDashboardUrl);

        res.render('results', {
            bmiText: bmiText,
            cancerRisk: cancerRisk,
            heartDiseaseRisk: heartDiseaseRisk,
            tableauCancerDashboardUrl: tableauCancerDashboardUrl,
            tableauHeartDashboardUrl: tableauHeartDashboardUrl
        });
    } catch (err) {
        console.error('Error:', err);
        res.status(500).send('Oops, something went wrong!');
    }
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});
