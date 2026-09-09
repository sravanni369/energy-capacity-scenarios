from pathlib import Path
import json,hashlib,sys
import pandas as pd
src=Path(sys.argv[1])
out=Path(__file__).resolve().parent;(out/'data').mkdir(parents=True,exist_ok=True);(out/'results').mkdir(exist_ok=True)
df=pd.read_csv(src); df.columns=df.columns.str.strip()
print(df.columns.tolist())
df['DateTime']=pd.to_datetime(df.DateTime,format='%m/%d/%Y %H:%M',errors='raise')
assert not df.isna().any().any();assert not df.DateTime.duplicated().any()
df=df.sort_values('DateTime'); zone=[c for c in df if 'PowerConsumption' in c.replace(' ','')]
assert len(zone)==3
df['total']=df[zone].sum(axis=1)
assert df.total.gt(0).all()
median=float(df.total.median())
df['load_index']=100*df.total/median
clean=df[['DateTime','Temperature','Humidity','Wind Speed','load_index']]
clean.to_csv(out/'data/demand_weather.csv',index=False,float_format='%.9f')
audit={'rows':len(df),'missing_cells':int(df.isna().sum().sum()),'duplicate_timestamps':0,'first':str(df.DateTime.min()),'last':str(df.DateTime.max()),'time_step_counts_seconds':df.DateTime.diff().dt.total_seconds().value_counts().to_dict(),'day_counts':df.groupby(df.DateTime.dt.date).size().value_counts().to_dict(),'total_load_median_source_units':median,'normalization':'100 * sum of three zone readings / full-sample median sum','units':'Normalized index; UCI variable table leaves physical units unspecified','sha256_raw_csv':hashlib.sha256(src.read_bytes()).hexdigest(),'source_url':'https://archive.ics.uci.edu/dataset/849/power+consumption+of+tetouan+city'}
(out/'results/data_audit.json').write_text(json.dumps(audit,indent=2));print(json.dumps(audit,indent=2))
