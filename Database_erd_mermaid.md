erDiagram
  PATIENT {
    uuid patient_id PK
    string first_name
    string last_name
    date dob
    string gender
    string race
    string ssn
    string medicare_beneficiary_id
    string phone
    string email
    string street_address
    string address_line2
    string city
    string state
    string postal_code
    float latitude
    float longitude
    timestamp created_at
    timestamp updated_at
    uuid shard_key
  }

  FACILITY {
    uuid facility_id PK
    string hospital_npi
    string name
    string street_address
    string address_line2
    string city
    string state
    string postal_code
    timestamp created_at
    timestamp updated_at
  }

  PROVIDER {
    uuid provider_id PK
    string first_name
    string last_name
    string job_title
    string department
    uuid facility_id FK
    timestamp created_at
    timestamp updated_at
  }

  ICD10_DIAGNOSIS {
    string icd10_code PK
    string short_desc
    string long_desc
  }

  ICD10_PROCEDURE {
    string icd10_proc_code PK
    string short_desc
    string long_desc
  }

  HCPCS {
    string hcpcs_code PK
    string name
  }

  MEDICATION_NDC {
    string ndc_code PK
    string drug_generic
    string drug_brand
    string drug_company
  }

  APPOINTMENT {
    uuid appointment_id PK
    uuid patient_id FK
    uuid provider_id FK
    uuid facility_id FK
    timestamp scheduled_at
    timestamp start_at
    timestamp end_at
    string reason
    string status
    timestamp created_at
    timestamp updated_at
  }

  ENCOUNTER {
    uuid encounter_id PK
    uuid patient_id FK
    uuid provider_id FK
    uuid facility_id FK
    string encounter_type
    timestamp start_at
    timestamp end_at
    string visit_number
    timestamp created_at
    timestamp updated_at
  }

  ENCOUNTER_DIAGNOSIS {
    uuid enc_diagnosis_id PK
    uuid encounter_id FK
    string icd10_code FK
    int sequence
    boolean present_on_admission
  }

  ENCOUNTER_PROCEDURE {
    uuid enc_procedure_id PK
    uuid encounter_id FK
    string icd10_proc_code FK
    int sequence
  }

  MEDICATION_ORDER {
    uuid med_order_id PK
    uuid encounter_id FK
    uuid patient_id FK
    string ndc_code FK
    string dose
    string route
    string frequency
    date start_date
    date end_date
    string status
    timestamp created_at
    timestamp updated_at
  }

  BILLING_CLAIM {
    uuid claim_id PK
    uuid encounter_id FK
    uuid patient_id FK
    string payer_ein
    string payer_duns
    string currency_code
    decimal total_amount
    string status
    timestamp submitted_at
    timestamp paid_at
    timestamp created_at
    timestamp updated_at
  }

  CLAIM_LINE {
    uuid claim_line_id PK
    uuid claim_id FK
    string hcpcs_code FK
    string icd10_proc_code
    int units
    decimal unit_price
    decimal line_amount
  }

  ROUTER_SHARD_MAP {
    int shard_id PK
    string range_start
    string range_end
    string ag_listener_dsn
    string read_only_routing_url
    string write_primary_url
    boolean active
    timestamp updated_at
  }

  USER_ACCOUNT {
    uuid user_id PK
    string username
    string password_hash
    string email
    string display_name
    string role
    boolean active
    timestamp created_at
    timestamp updated_at
  }

  PATIENT_USER {
    uuid user_id PK
    uuid patient_id
  }

  CLINICIAN_USER {
    uuid user_id PK
    uuid provider_id
  }

  CLINICIAN_FACILITY {
    uuid clf_id PK
    uuid user_id
    uuid facility_id
  }

  AUDIT_EVENT {
    uuid audit_id PK
    uuid request_id
    uuid user_id
    string role
    string action
    string object_type
    string object_id
    string before_json
    string after_json
    timestamp happened_at
  }

  PATIENT ||--o{ APPOINTMENT : has
  PROVIDER ||--o{ APPOINTMENT : scheduled_with
  FACILITY ||--o{ APPOINTMENT : at

  PATIENT ||--o{ ENCOUNTER : has
  PROVIDER ||--o{ ENCOUNTER : performs
  FACILITY ||--o{ ENCOUNTER : occurs_at

  ENCOUNTER ||--o{ ENCOUNTER_DIAGNOSIS : coded_by
  ICD10_DIAGNOSIS ||--o{ ENCOUNTER_DIAGNOSIS : referenced

  ENCOUNTER ||--o{ ENCOUNTER_PROCEDURE : coded_by
  ICD10_PROCEDURE ||--o{ ENCOUNTER_PROCEDURE : referenced

  ENCOUNTER ||--o{ MEDICATION_ORDER : generates
  PATIENT ||--o{ MEDICATION_ORDER : receives
  MEDICATION_NDC ||--o{ MEDICATION_ORDER : uses_ndc

  PATIENT ||--o{ BILLING_CLAIM : billed_in
  ENCOUNTER ||--o{ BILLING_CLAIM : source
  BILLING_CLAIM ||--o{ CLAIM_LINE : has_lines
  HCPCS ||--o{ CLAIM_LINE : coded_with
  ICD10_PROCEDURE ||--o{ CLAIM_LINE : may_reference

  ROUTER_SHARD_MAP ||--o{ PATIENT : routes_by

  USER_ACCOUNT ||--o{ AUDIT_EVENT : actor
  USER_ACCOUNT ||--|| PATIENT_USER : is_patient
  PATIENT ||--|| PATIENT_USER : owned_by

  USER_ACCOUNT ||--|| CLINICIAN_USER : is_clinician
  CLINICIAN_USER ||--|| PROVIDER : maps_to
  USER_ACCOUNT ||--o{ CLINICIAN_FACILITY : affiliated_with
  FACILITY ||--o{ CLINICIAN_FACILITY : has_clinicians
