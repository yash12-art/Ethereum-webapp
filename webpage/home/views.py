import requests
from django.shortcuts import render

def fetch_ethereum(request):
    if request.method == 'POST':
        ethereum_address = request.POST.get('ethereum_address')
        url = f'https://api.etherscan.io/api?module=account&action=balance&address={ethereum_address}&tag=latest&apikey=YOUR_API_KEY'
        
        response = requests.get(url)
        balance = response.json().get('result')

        url = f'https://api.etherscan.io/api?module=account&action=txlist&address={ethereum_address}&startblock=0&endblock=99999999&page=1&offset=5&sort=desc&apikey=YOUR_API_KEY'
        
        response = requests.get(url)
        transactions = response.json().get('result')

        context = {
            'balance': balance,
            'transactions': transactions,
        }
        return render(request, 'fetch.html', context)

    return render(request, 'index.html')
