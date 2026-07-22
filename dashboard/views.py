from django.shortcuts import render

# Données mockées pour les templates (seront remplacées par des queries ORM)
MOCK_USERS = [
    {'name': 'Amine Mansouri', 'email': 'a.mansouri@xyz.ma', 'role': 'Super Admin',        'dept': 'DSI',          'status': 'actif',   'last_login': 'Auj. 09:15',  'avatar': 'AM', 'requests': 12, 'color': '#7C3AED'},
    {'name': 'Sara El Fassi',  'email': 's.elfassi@xyz.ma',  'role': 'RSSI',              'dept': 'SSI',          'status': 'actif',   'last_login': 'Auj. 08:42',  'avatar': 'SE', 'requests': 4,  'color': '#EF4444'},
    {'name': 'Karim Berrada',  'email': 'k.berrada@xyz.ma',  'role': 'Responsable IT',    'dept': 'DSI',          'status': 'actif',   'last_login': 'Hier 17:30',  'avatar': 'KB', 'requests': 2,  'color': '#0EA5E9'},
    {'name': 'Nadia Benchekroun','email': 'n.benchekroun@xyz.ma','role': 'Technicienne Réseau','dept': 'Infra',       'status': 'actif',   'last_login': '18 juil.',    'avatar': 'NB', 'requests': 8,  'color': '#10B981'},
    {'name': 'Rachid Qorchi',  'email': 'r.qorchi@xyz.ma',  'role': 'Gestionnaire RH',   'dept': 'RH',           'status': 'inactif', 'last_login': '2 juil.',    'avatar': 'RQ', 'requests': 3,  'color': '#06B6D4'},
    {'name': 'Fatima Zahrae',  'email': 'f.zahrae@xyz.ma',  'role': 'Développeuse',      'dept': 'Dev',          'status': 'actif',   'last_login': 'Hier 14:22',  'avatar': 'FZ', 'requests': 7,  'color': '#8B5CF6'},
    {'name': 'Youssef Tazi',   'email': 'y.tazi@xyz.ma',    'role': 'Administrateur IAM','dept': 'Sécu.',      'status': 'actif',   'last_login': 'Auj. 07:55',  'avatar': 'YT', 'requests': 19, 'color': '#F59E0B'},
]

MOCK_CHART_DATA = [
    ('Jan', '25%', False), ('Fév', '30%', False), ('Mar', '20%', False),
    ('Avr', '40%', False), ('Mai', '35%', False), ('Jun', '50%', False), ('Jul', '38%', True),
]

MOCK_WORKFLOWS = [
    'Standard (3 étapes)',
    'Accès critique (5 étapes)',
    'Urgence validée',
    'Accès temporaire',
]

def login_view(request):
    return render(request, 'sgdh/login.html')

def dashboard_view(request):
    return render(request, 'sgdh/dashboard.html')

def new_request_view(request):
    steps = [
        (1, 'Identification'),
        (2, 'Ressource & accès'),
        (3, 'Justification'),
        (4, 'Récapitulatif'),
    ]
    request_types = ['Application', 'Dossier réseau', 'Zone physique']
    access_levels = ['Lecture', 'Lecture/Écriture', 'Administration']
    current_step = int(request.GET.get('step', 1))
    selected_type = request.GET.get('request_type', '')
    selected_level = request.GET.get('access_level', '')
    return render(request, 'sgdh/new_request.html', {
        'steps': steps,
        'request_types': request_types,
        'access_levels': access_levels,
        'current_step': current_step,
        'selected_type': selected_type,
        'selected_level': selected_level,
    })

def requests_list_view(request):
    return render(request, 'sgdh/requests_list.html')

def validation_queue_view(request):
    return render(request, 'sgdh/validation_queue.html')

def audit_view(request):
    return render(request, 'sgdh/audit.html', {
        'chart_data': MOCK_CHART_DATA,
    })

def workflow_view(request):
    return render(request, 'sgdh/workflow.html', {
        'workflows': MOCK_WORKFLOWS,
    })

def users_view(request):
    return render(request, 'sgdh/users.html', {
        'users': MOCK_USERS,
    })

def settings_view(request):
    return render(request, 'sgdh/settings.html')
