// code for referenc
import requests

url = "https://app.rockgympro.com/b/widget/?a=equery"

payload='offering_guid=e9471c8dd372431dbb24239b23dd9b64&show_date=2021-01-21'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'AWSELB=A5EDC1071EB54DEE085FA9BC53DB5910EF75B9C87F1017073E8B0D71F097020F81072E969926CF7FF56E9A38BD28DD45BF4041CDE064EAF6E07C2B6B89192D65362084B355; AWSELBCORS=A5EDC1071EB54DEE085FA9BC53DB5910EF75B9C87F1017073E8B0D71F097020F81072E969926CF7FF56E9A38BD28DD45BF4041CDE064EAF6E07C2B6B89192D65362084B355; RGPSessionGUID=05fce808c16c665d8d69e1fea0c2cef5b067273ffa14993ccb867431b876640439acaae33d2d07efee6116f3050689c8; RGPPortalSessionID=ggdbov9d7h94jh6kin579bg886; BrowserSessionId=6007c40288034'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

// inspect response.json()["event_list_html"]...
// html table, for each row: first TD is session time, second TD is availability, 
'''
{
    "error_messages": "",
    "has_promo_code": true,
    "promo_code_is_valid": false,
    "promo_code_error_message": "",
    "event_list_html": "..."
    "date_label": "Date Selected:&nbsp;<span id=\"offering-page-selected-long-date\">Thu, January 21</span>"
}
<table id='offering-page-select-events-table'\">
  <tr>
    <td class='offering-page-schedule-list-time-column'>
      Thu, January 21, 3:30 PM to  5:30 PM
    </td>
    <td>
      <strong>Availability</strong>
      <br>
      29 spaces
     </td>
    <td></td>
    <td><a>Select</a>\n</td>
   </tr>
   <tr>
    <td class='offering-page-schedule-list-time-column'>
      Thu, January 21, 5:45 PM to  7:45 PM
    </td>
    <td>
      <strong>Availability</strong>
      <br>
      <div class='offering-page-event-is-full'>Full.&nbsp;Please make a different selection.</div>
     </td>
     <td></td>
     <td>
     </td>
    </tr>
  </table>",
'''
