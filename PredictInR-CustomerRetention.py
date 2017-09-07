
def get_customer_retention(params)
r.assign('PersonsCovered', params['PersonsCovered'])
r.assign('tw304_scale', params['tw304_scale'])
r.assign('tenure', params['tenure'])
r.assign('Age', params['Age'])
r.assign('hstatus', params['hstatus'])
r.assign('pay_mh_1', params['pay_mh_1'])
r.assign('pay_fr_1', params['pay_fr_1'])
r.assign('tw304_rate_code', params['tw304_rate_code'])
r.assign('rebate_type', params['rebate_type'])
r.assign('rebate_perc', params['rebate_perc'])
r.assign('income_tier', params['income_tier'])
r.assign('Prod_2_Type', params['Prod_2_Type'])
r.assign('Prod_3_Type', params['Prod_3_Type'])
r.assign('Prodcategory', params['Prodcategory'])
r.assign('Residential_Pcode', params['Residential_Pcode'])
r.assign('Residential_State', params['Residential_State'])
r.assign('gender', params['gender'])
r.assign('EAS', params['EAS'])
r.assign('EDS', params['EDS'])
r.assign('ERS', params['ERS'])
r.assign('EOS', params['EOS'])
r.assign('Population', params['Population'])

	
cust.policy <- data.frame(PersonsCovered=PersonsCovered, tw304_scale=tw304_scale, tenure=tenure, Age=Age, hstatus=hstatus, pay_mh_1=pay_mh_1, pay_fr_1=pay_fr_1, tw304_rate_code=tw304_rate_code, rebate_type=rebate_type, rebate_perc=rebate_perc, income_tier=income_tier, Prod_2_Type=Prod_2_Type, Prod_3_Type=Prod_3_Type, Prodcategory=Prodcategory, Residential_Pcode=Residential_Pcode, Residential_State=Residential_State, gender=gender, PersonsCovered=PersonsCovered, EAS=EAS, EDS=EDS, ERS=ERS, EOS=EOS, Population=Population)
PersonCover=1, tw304_scale="S", tenure=36, Age=36, hstatus="A", pay_mh_1="B", pay_fr_1="Q", tw304_rate_code=0, rebate_type="RB", rebate_perc=30, income_tier=0, Prod_2_Type="Care N Repair", Prod_3_Type="", Prodcategory="Combination", Residential_Pcode=2020, Residential_State="NSW", gender="M", EAS=1021, EDS=1013, ERS=994, EOS=1022, Population=10178)
{
	
	"PersonsCover":1,
	"tw304_scale":"S", 
	"tenure":36,
	"Age":36, 
	"hstatus":"A", 
	"pay_mh_1":"B", 
	"pay_fr_1":"Q", 
	"tw304_rate_code":0, 
	"rebate_type":"RB", 
	"rebate_perc":30, 
	"income_tier":0, 
	"Prod_2_Type":"Care N Repair", 
	"Prod_3_Type":"", 
	"Prodcategory":"Combination", 
	"Residential_Pcode":2020, 
	"Residential_State":"NSW", "gender":"M", 
	"PersonsCovered":1, 
	"EAS":1021,
	"EDS":1013, 
	"ERS":994,
	"EOS":1022, 
	"Population":10178
}