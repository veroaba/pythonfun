from math import exp

def fit(xvalues, yvalues):
    """
    Fits the data and returns the parameter in a tuple.
    Currently returns hard-coded values as a mock.
    TODO: implement logistic regression.

    Inputs
    -------

    xvalues: the independent variable
    yvalues: the dependent variable 

    Returns
    -------

    A tuple of parameters obtained in the fit.
    """
    slope, intercept = (9.812037170985635, 5.175316482607568)
    return slope, intercept

def predict_proba_maker (slope, intercept):
    "makes a function that returns probabilities"
    def inner(xvalues):
        "returns probabilities given the independent variable"
        # return probabilities using the sigmoid function
        probabilities = [ 1/(1 + exp(-(intercept + slope * x))) for x in xvalues]
        return probabilities 
    return inner 


def predict_maker(slope, intercept):
    "makes a prediction function"
    def inner(xvalues, t= 0.5):
        "predicts 1 or 0 for a threshold t, default 0.5"
        predict_proba = predict_proba_maker(slope, intercept)
        probabilities = predict_proba(xvalues)
        # compare to threshold t..1*false gives you 0
        predictions = [1*(p >= t) for p in probabilities ]
        return predictions
    return inner 

def model():
    parameters = {}
    def inner_probabilities(xvalues):
        "returns probabilities given the independent variable"
        intercept = parameters ['intercept']
        slope = parameters ['slope']
        # return probabilities using the sigmoid function
        probabilities = [ 1/(1 + exp(-(intercept + slope * x))) for x in xvalues]

        return probabilities 

    def inner_predictions(xvalues, t= 0.5):
        "predicts 1 or 0 for a threshold t, default 0.5"
        intercept = parameters ['intercept']
        slope = parameters ['slope']
        probabilities = inner_probabilities(xvalues)
        # compare to threshold t..1*false gives you 0
        predictions = [1*(p >= t) for p in probabilities ]
        return predictions
    
    def inner_fit(xvalues, yvalues):
        """
        Fits the data and returns the parameter in a tuple.
        Currently returns hard-coded values as a mock.
        TODO: implement logistic regression.
    
        Inputs
        -------
    
        xvalues: the independent variable
        yvalues: the dependent variable 
    
        Returns
        -------
    
        A tuple of parameters obtained in the fit.
        """
        slope, intercept = (9.812037170985635, 5.175316482607568)
        parameters ['slope'] = slope
        parameters ['intercept'] = intercept
    methods = dict (
        fit = inner_fit,
        predict_proba = inner_probabilities, 
        predict = inner_predictions
    )
    return methods 
class AbstractModel:

    def __innit__(self):
        self.probabilities = None
        slef.predictions = None
        
    def fit(self, xvalues, yvalues):
        raise NotImplementedYetError
        
    def predict_proba(self, xvalues):
        raise NotImplementedYetError

    def predict(self, xvalues, t=0.5):
        "predict 1 or 0 for a threshold t, default 0.5"
         probabilities = self.predict_proba(xvalues)
        # compare to threshold t..1*false gives you 0
        self.predictions = [1*(p >= t) for p in probabilities]
        return self.predictions

class LogicticModel(AbstractModel):
   
    def __init__(self):
        super().__init__()
        self.slope = None
        self.intercept = None

    def fit(self, xvalues, yvalues):
        """
        Fits the data and returns the parameter in a tuple.
        Currently returns hard-coded values as a mock.
        TODO: implement logistic regression.
    
        Inputs
        -------
    
        xvalues: the independent variable
        yvalues: the dependent variable 
    
        Returns
        -------
    
        A tuple of parameters obtained in the fit.
        """
        self.slope, self.intercept = (9.812037170985635, 5.175316482607568)
    def predict_proba(self, xvalues):
        "returns probabilities given the independent variable"
        # return probabilities using the sigmoid function
        probabilities = [ 1/(1 + exp(-(self.intercept + self.slope * x))) for x in xvalues]
        return probabilities
    
   