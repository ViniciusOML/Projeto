# -*- encoding: utf-8 -*-
import io
from reportlab.pdfgen import canvas

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
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
        context = relatorio_consultas_por_cid_post(request)
        if request.POST['pdf'] == '1':
            return relatorio_consultas_por_cid_pdf(request, context)
    cids = Cid.objects.all()

    context['cids'] = cids
    return render(request, 'relatorios/consultas_por_cid.html', context)


def relatorio_consultas_por_cid_post(request):
    context = {
        'consultas': []
    }

    if request.method == "POST":
        consultas = Consulta.objects.filter(data_consulta__range=(request.POST['data_inicial'], request.POST['data_final']))

        cids = request.POST.getlist("cids")

        context['data_inicial'] = request.POST['data_inicial']
        context['data_final'] = request.POST['data_final']
        context['cids_selecionados'] = request.POST.getlist("cids")

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
                    if resultado.cid.codigo_cid not in cids:
                        continue
                context['consultas'].append({
                    'data': consulta.data_consulta,
                    'paciente': consulta.atendimento.paciente.nome_completo,
                    'codigo_lif': consulta.atendimento.codigo_lif,
                    'lif': consulta.atendimento.lif.nome_lif,
                    'procedimento': consulta.procedimento.nome_procedimento,
                    'codigo_cid': resultado.cid.codigo_cid,
                    'url': url,
                })
    
    return context

def relatorio_consultas_por_cid_pdf(request, context):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    linha = 700
    for consulta in context['consultas']:
        p.drawString(10, linha, consulta['data'].strftime("%d/%m/%Y"))
        p.drawString(50, linha, consulta['paciente'])
        linha -= 15

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')