from pyflowchart import Flowchart

code = """
start: Start
op1: Generate Mobile Usage Audit Report from Mobileum platform for main data sources
op2: Analyze usage reports and validation
op3: Review and confirm reported CDRs in the HLR
op4: Report usage deviations and missing transactions to OCS via Jira system
op5: Analyze and deploy deviations in Mobileum through mediation and fix missing transactions
op6: Validate corrective action taken by Opennet, monitor missing transactions, and identify new deviations
end: End

start->op1->op2->op3->op4->op5->op6->end
"""

chart = Flowchart.from_code(code)
chart.flowchart()
