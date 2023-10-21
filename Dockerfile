FROM mwalbeck/python-poetry:3.12
COPY . .
RUN poetry add shap

