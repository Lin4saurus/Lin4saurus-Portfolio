# Genera los HTML y los imprime a PDF con Edge.
# Uso: powershell -ExecutionPolicy Bypass -File imprimir.ps1
# Si un PDF está abierto en otro programa, ciérralo y vuelve a correr esto.
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$destino = Split-Path -Parent $aqui
$edge = "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
python "$aqui\generar.py"
foreach ($p in @(@('cv-es.html', 'Carolina_Aranibar_CV_ES.pdf'), @('cv-en.html', 'Carolina_Aranibar_CV_EN.pdf'))) {
  $src = "file:///" + ("$aqui\" + $p[0]).Replace('\', '/')
  $tmp = Join-Path $env:TEMP ("cv_" + $p[1])
  $out = "$destino\" + $p[1]
  & $edge --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 "--print-to-pdf=$tmp" $src 2>$null | Out-Null
  try {
    Copy-Item $tmp $out -Force -ErrorAction Stop
    Write-Output "OK  $out"
  } catch {
    Write-Output "NO SE PUDO ACTUALIZAR $out (está abierto en otro programa; ciérralo y vuelve a correr esto)"
  }
}
