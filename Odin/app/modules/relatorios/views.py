# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import JsonResponse
from ...models import \
    ResultadoAudiometria,\
    ResultadoBera,\
    ResultadoPac,\
    ResultadoPadrao,\
    Consulta,\
    Cid


@login_required(login_url='/login')
@permission_required(login_url='/login',perm=('app.view_consulta',\
    'app.view_resultadobera',\
    'app.view_resultadoaudiometria',\
    'app.view_resultadopac',\
    'app.view_resultadopadrao',))
def relatorio_consultas_por_cid(request):
    context = {}
    
    if request.method == "POST":
        return relatorio_consultas_por_cid_api(request)
    cids = Cid.objects.all()

    context['cids'] = cids
    return render(request, 'relatorios/consultas_por_cid.html', context)


def relatorio_consultas_por_cid_api(request):
    context = {
        'consultas': []
    }

    if request.method == "POST":
        consultas = Consulta.objects.filter(data_consulta__range=(request.POST['data_inicial'], request.POST['data_final']))

        cids = request.POST.getlist("cids[]")
        for consulta in consultas:
            url = ''

            if consulta.procedimento.tipo_laudo == 'BERA':
                resultados = ResultadoBera.objects.filter(consulta_id=consulta.id)
            elif consulta.procedimento.tipo_laudo == 'PAC':
                resultados = ResultadoPac.objects.filter(consulta_id=consulta.id)
            elif consulta.procedimento.tipo_laudo == 'AUDIOMETRIA':
                resultados = ResultadoAudiometria.objects.filter(consulta_id=consulta.id)
            else:
                resultados = ResultadoPadrao.objects.filter(consulta_id=consulta.id)

            for resultado in resultados:
                if consulta.procedimento.tipo_laudo == 'BERA':
                    url = '/resultados_bera/show/' + str(resultado.id) + '/'
                elif consulta.procedimento.tipo_laudo == 'PAC':
                    url = '/resultados_pac/show/' + str(resultado.id) + '/'
                elif consulta.procedimento.tipo_laudo == 'AUDIOMETRIA':
                    url = '/resultados_audiometria/show/' + str(resultado.id) + '/'
                else:
                    url = '/resultados_padrao/show/' + str(resultado.id) + '/'

                if len(cids) > 0:
                    if str(resultado.cid.id) not in cids:
                        continue
                context['consultas'].append({
                    'data': consulta.data_consulta.strftime("%d/%m/%Y"),
                    'paciente': consulta.atendimento.paciente.nome_completo,
                    'codigo_lif': consulta.atendimento.codigo_lif,
                    'lif': consulta.atendimento.lif.nome_lif,
                    'procedimento': consulta.procedimento.nome_procedimento,
                    'codigo_cid': resultado.cid.codigo_cid,
                    'url': url,
                })
    
    return JsonResponse(context)