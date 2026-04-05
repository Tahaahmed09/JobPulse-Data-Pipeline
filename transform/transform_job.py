import pandas as pd

def clean_nested_columns(df):
    df['location'] = df['location'].apply(lambda x: x.get('display_name') if isinstance(x, dict) else None)
    df['company'] = df['company'].apply(lambda x: x.get('display_name') if isinstance(x, dict) else None)
    return df

def filter_data(df):
    df = df[df['salary_min'].notnull()]
    df = df[df['description'].notnull()]
    df = df[df['title'].str.contains("Data", case=False, na=False)]
    return df

def add_remove_features(df):
    # Salary calculations
    df['avg_yearly_salary'] = (df['salary_min'] + df['salary_max']) / 2
    df['avg_monthly_salary'] = (df['avg_yearly_salary'] / 12).round(2)

    # Date
    df['posted_date'] = pd.to_datetime(df['created']).dt.date

    # Metadata
    df['currency'] = 'USD'

    # Drop unused column
    df.drop(columns=['created'], inplace=True, errors='ignore')
    return df

def extract_skills(desc):
    skills = []
    if 'python' in desc.lower():
        skills.append('Python')
    if 'sql' in desc.lower():
        skills.append('SQL')
    if 'aws' in desc.lower():
        skills.append('AWS')
    if 'cloud' in desc.lower():
        skills.append('Cloud')
    if 'airflow' in desc.lower():
        skills.append('AirFlow')
    return ", ".join(skills)

def apply_skills(df):
    df['skills'] = df['description'].apply(
        lambda x: extract_skills(x) if isinstance(x, str) else ""
    )
    return df

def remove_duplicates(df):
    return df.drop_duplicates(subset=['title','company','posted_date'])

def transform_jobs(data):
    df = pd.DataFrame(data)

    df = df[['title', 'description', 'location', 'company', 'salary_min', 'salary_max', 'created']]

    df = clean_nested_columns(df)
    df = filter_data(df)
    df = add_remove_features(df)
    df = apply_skills(df)
    df = remove_duplicates(df)

    return df
