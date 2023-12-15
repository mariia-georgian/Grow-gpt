import fewshot.fewshotutility as fewshotutility
import fewshot.fewshot as fewshot
import pandas as pd
from langchain.globals import set_debug
# set_debug(True)


if __name__ == '__main__':
    examples = fewshot.FewShot.get_examples()
    prefix = fewshot.FewShot.get_prefix()
    suffix = fewshot.FewShot.get_suffix()
    example_template, example_variables = fewshot.FewShot.get_example_template()

    fewShot = fewshotutility.FewShotUtility(examples=examples,
                                            prefix=prefix,
                                            suffix=suffix,
                                            input_variables=["input"],
                                            example_template=example_template,
                                            example_variables=example_variables
                                            )
 
    df_test = pd.read_csv('test.csv')
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    k = 0
    for p in df_test[:100].iterrows():
        
        prompt = fewShot.get_prompt(str(p[1]['instructions']).replace('{', '').replace('}', '')).replace('Lead Converted: ', '')
        ans = fewShot.send_prompt_llama(prompt)

        ans = 'True' in ans
        if ans and p[1]['labels'] is True:
            tp += 1
        elif ans and p[1]['labels'] is False:
            fp += 1
        elif ans is False and p[1]['labels'] is False:
            tn += 1
        elif ans is False and p[1]['labels'] is True:
            fn += 1
      
    print(tp, fp, fn, tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    print(f'precision: {precision}')
    print(f'recall: {recall}')
