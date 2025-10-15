import hl7
import json

def hl7_to_json(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    message = hl7.parse(data)
    msg_dict = {}

    for segment in message:
        seg_name = segment[0][0]
        msg_dict[seg_name] = []
        fields = []
        for field in segment[1:]:
            fields.append(str(field))
        msg_dict[seg_name].append(fields)

    json_output = json.dumps(msg_dict, indent=4)
    return json_output

if __name__ == "__main__":
    json_data = hl7_to_json('sample_adt.hl7')
    with open('adt_message.json', 'w') as f:
        f.write(json_data)
    print("HL7 message converted to JSON successfully.")
