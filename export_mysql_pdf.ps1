$docxPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-csdl-mysql-workbench\Bao_Cao_Thuc_Hanh_Tao_CSDL_MySQL_Workbench.docx"
$pdfPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-csdl-mysql-workbench\Bao_Cao_Thuc_Hanh_Tao_CSDL_MySQL_Workbench.pdf"

Write-Host "Converting MySQL DOCX to PDF using Word COM..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docxPath)
    $wdFormatPDF = 17
    $doc.SaveAs([ref]$pdfPath, [ref]$wdFormatPDF)
    $doc.Close([ref]$false)
    Write-Host "PDF export successful: $pdfPath"
}
catch {
    Write-Error $_
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
