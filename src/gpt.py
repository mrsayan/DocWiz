import openai
import os


class GPTDocGen:
    def __init__(self, openai_api_key : str) -> None:
        self.opeai_api_key = openai_api_key

    def getResp(self, prompt):
        openai.api_key = self.opeai_api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response["choices"][0]["text"]


    def getTextGPT(self, info):
        return {
                "overview": self.getResp("Explain this problem statement properly: " + info["overview"]),
                "data_prep": self.getResp("Explain the steps taken in data preparations properly: " + info["data_prep"]),
                "model_name": info["model_name"],
                "model_methadology": self.getResp("Explain this public information given properly: " + info["model_methadology"] + info["model_name"]),
                "assumptions": self.getResp("Explain this assumptions properly: " + info["assumptions"]),
                "conclusion": self.getResp("Explain this reason for assumptions properly: " +
                                    info["conclusion"] +
                                    info["overview"] +
                                    info["data_prep"] +
                                    info["model_name"] +
                                    info["model_methadology"] +
                                    info["assumptions"]
                                    )
            }
