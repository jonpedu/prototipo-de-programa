# Script de Inicializacao da Aplicacao de Analise de Dados Ambientais
# Execute este script com: .\iniciar.ps1

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ANALISE DE DADOS AMBIENTAIS" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se o Python esta instalado
Write-Host "[1/3] Verificando instalacao do Python..." -ForegroundColor Yellow
try {
    $pythonVersion = py --version 2>&1
    Write-Host "      [OK] Python encontrado: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "      [ERRO] Python nao encontrado!" -ForegroundColor Red
    Write-Host "      Por favor, instale Python 3.8 ou superior." -ForegroundColor Red
    Write-Host "      Download: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit
}

Write-Host ""

# Verificar se as dependencias estao instaladas
Write-Host "[2/3] Verificando dependencias..." -ForegroundColor Yellow
$streamlitInstalled = py -m pip list 2>&1 | Select-String "streamlit"

if (-not $streamlitInstalled) {
    Write-Host "      [AVISO] Dependencias nao encontradas. Instalando..." -ForegroundColor Yellow
    Write-Host ""
    py -m pip install -r requirements.txt
    Write-Host ""
    Write-Host "      [OK] Dependencias instaladas com sucesso!" -ForegroundColor Green
}
else {
    Write-Host "      [OK] Dependencias ja instaladas" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  INICIANDO APLICACAO..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[3/3] A aplicacao abrira automaticamente no navegador" -ForegroundColor Yellow
Write-Host "      URL: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "      [DICA] Para encerrar, pressione Ctrl+C" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Iniciar o Streamlit
py -m streamlit run app.py
