import json
import streamlit as st


class ModelDataInfo:
    def __init__(self):
        """Fetches all the required information about the model and datasets
        """
        self._defaults = {
            "overview": "The Credit Line Decrease (CLD) model is used to identify high risks accounts with\nthe objective to mitigate potential losses by decreasing their credit limit. The\nmodel will be used on all the RRB credit card customers. ",
            "data_prep": "The model has been developed using the extracts from the Card Master File\n(CMF). Given that the development of the model was priority based for the\nbusiness based on the impact analysis of quick model developed earlier, a\nlimited set of features were used from a previous model (APD model).",
            "model_name": "XGBoost:v1.0.0",
            "model_methadology": "XGBoost and Logistic Regression are two techniques used for creating the model\nalong with GBM trees. The final model is built using XGBoost and this is\ndetermined based on the performance benefits observed in using XGBoost.",
            "assumptions": "The model has been built on both internal as well as external data. The external\ncredit bureau data is received monthly through a batch process for the Existing\nCard Members (ECM). In addition, the model leverages daily data \u2013 daily\nbureau (in addition to batch bureau), daily triggers and a few daily on-us\nattributes \u2013 to allow the identification of high risk accounts before they utilize the\nremaining open-to-buy amount.",
            "conclusion": "The model Risk Score shows incremental model performance compared to other\nbenchmarks. While there is no direct benchmark available for the CLD model\nsince it\u2019s a bespoke score, it is still compared to the other scores, since they are\nbeing used in the current CLD policy. "
        }

    def get_document_general_info(self):
        """Collectes the information from the user about
        - Given data
        - Approaches
        - Model approaches
        - Assumptions
        - Conclusion
        """

        info_json = {}
        st.title("Add Public and Model Informationn")

        self.overview = st.text_area(
            "Write a small overview of the problem statement", placeholder=self._defaults['overview']
        )
        self.data_prep = st.text_area("Data preparation approaches", placeholder=self._defaults['data_prep'])

        self.model_name = st.text_input("Model name and info: ", placeholder=self._defaults['model_name'])
        self.model_methadology = st.text_area("Model methadology: ", placeholder=self._defaults['model_methadology'])

        # show a model performance report in dataframe

        self.assumptions = st.text_area("Assumptions", placeholder=self._defaults['assumptions'])
        self.assumption_reasons = st.text_area("Reason for above decisions", placeholder="Optional")
        self.conclusion = st.text_area("Add any of your conclusions", placeholder=self._defaults['conclusion'])

        if self.overview:
            info_json["overview"] = self.overview

        if self.data_prep:
            info_json["data_prep"] = self.data_prep

        if self.model_name:
            info_json["model_name"] = self.model_name

        if self.model_methadology:
            info_json["model_methadology"] = self.model_methadology

        if self.assumptions:
            info_json["assumptions"] = self.assumptions

        if self.conclusion:
            info_json["conclusion"] = self.conclusion

        # Add a submit button
        if st.button("Submit"):
            st.write("Noted all your observations and assumptions")
            with open("Data/info_json.json", "w") as outfile:
                json.dump(info_json, outfile, indent=4)
            st.success("Noted all your assumptions and observations")
