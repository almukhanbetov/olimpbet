from bs4 import BeautifulSoup

html_content = '''<tr class="hi">
    <td width="20%" align="center">
        <div style="float: left;">
            <a class="ishodCount 81256127" href="javascript:loadadd(81256127, 2, 2);"><img id="i81256127" src="/img/plus.jpg" /> (+558) </a>
        </div>
        22:45
    </td>
    <td width="80%" style="border-right: 0 !important;">
        <div class="gameRel clearfix">
            <div class="gameNameLine">
                <font class="m">
                    <b>
                        <span style="position: relative;" id="match_live_name_81256127">
                            <a line="" style="text-decoration: none;" href="/index.php?page=line&amp;addons=1&amp;action=2&amp;mid=81256127">Рома - Брага</a>
                        </span>
                    </b>
                </font>
            </div>
        </div>
    </td>
</tr>
<tr>
    <td colspan="2">
        <div class="tab" id="odd81256129" data-match-id="81256129" data-match-count="5" data-cont="5" data-champ="7803344" data-sportid="1">
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">П1</span> -&nbsp;&nbsp;
                    <span class="bet_sel koefs" data-v1="3.46">
                        <b class="value_js"><span>3.46</span></b>
                    </span>
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Х</span> -&nbsp;&nbsp;
                    <span class="bet_sel koefs" data-v1="3.71">
                        <b class="value_js"><span>3.71</span></b>
                    </span>
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">П2</span> -&nbsp;&nbsp;
                    <span class="bet_sel koefs" data-v1="2.08">
                        <b class="value_js"><span>2.08</span></b>
                    </span>
                </span>
                &nbsp;
            </nobr>
        </div>
    </td>
</tr>'''

# Парсинг HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение информации о матче
match_info = soup.find('span', {'id': 'match_live_name_81256127'})
match_name = match_info.get_text(strip=True)

# Извлечение коэффициентов
odds_div = soup.find('div', {'class': 'tab', 'id': 'odd81256129'})
odds = []
for stat_issue in odds_div.find_all('span', {'class': 'googleStatIssue'}):
    bet_type = stat_issue.find('span', {'class': 'googleStatIssueName'}).get_text(strip=True)
    bet_value_tag = stat_issue.find('span', {'class': 'value_js'})
    if bet_value_tag:  # Проверка на None
        bet_value = bet_value_tag.get_text(strip=True)
        odds.append({
            'type': bet_type,
            'value': bet_value
        })

# Вывод данных
print(f"Матч: {match_name}")
print("Коэффициенты:")
for odd in odds:
    print(f"  {odd['type']}: {odd['value']}")
