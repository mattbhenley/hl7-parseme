# hl7-parseme

This project demonstrates how HL7 messages can be parsed, transformed, and routed between systems — similar to what an Interface Analyst does in a healthcare environment.

## Tools Used
- **Mirth Connect (NextGen Connect):** Integration engine for routing HL7 messages
- **Python (hl7apy):** Script to parse HL7 and convert to JSON
- **Sample HL7 Messages:** ADT^A01 (Admission) and ORU^R01 (Lab Results)

## Project Structure
hl7-parseme/
├── mirth_channels/ # exported Mirth channels
├── python_parser/ # Python parser and sample messages
├── screenshots/ # Mirth screenshots
└── README.md