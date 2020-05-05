from config_api import jprint, check_country
from pytest import mark


# тест для проверки запроса ежедневных значений
@mark.daily
def test_daily_req(api_request, list_of_pyt_adds):
    
    expected_first_date = list_of_pyt_adds[3] # значение из '--datefrom'
    expected_last_date = list_of_pyt_adds[4] # значение из '--dateto'
    
    # значение из фикстуры передается в аргументы функции check_country
    expected_country = check_country(list_of_pyt_adds[1]) # значение из '--country'
    
    assert api_request != [], f'\n\
            Возможно информация о стране "{expected_country}" отсуствует' # проверка, не является ли запрос пустым
    assert expected_first_date in api_request[0]['Date'] # ожидаемое первое значение даты
    assert expected_last_date in api_request[-1]['Date'] # ожидаемое последнее значение даты
    
    # проверка в цикле тк в данном запросе JSON объекты являются элементами списка
    for i in range(len(api_request)):
        jprint(api_request[i])
        
        assert api_request[i]['Country'] == expected_country # ожидаемая страна
        assert api_request[i]['Cases'] != '' # не является ли значение Cases пустой строкой
        
        # сравнение двух значений в строке Cases (нынешнее со следующим, в списке)
        if i + 1 == len(api_request):
            break
        assert api_request[i]['Cases'] <= api_request[i+1]['Cases'], f":: возможные сценарии возникновения ошибки \n\
                -даты идут не по порядку ({api_request[i-1]['Date']}, {api_request[i]['Date']}, {api_request[i+1]['Date']})\n\
                -требуется значение --province/--city для страны {expected_country}"
        

# тест для проверки запроса суммарных значений
@mark.sum
def test_sum_req(api_request, list_of_pyt_adds):
    expected_country = check_country(list_of_pyt_adds[1])
    assert api_request != []
    assert api_request[0]['Country'] == expected_country
    print('\n')
    jprint(api_request)