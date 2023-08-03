$input_dir = "D:/LianHui/Desktop"
$output_dir = "D:/LianHui/Desktop"

$files = Get-ChildItem -Path $input_dir -Filter "*.avi" -File

foreach ($file in $files) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    $output_file = Join-Path $output_dir ("${base}_deinterlaced.avi")

    & ffmpeg -i $file.FullName -vf yadif -c:v libx264 -crf 23 -c:a copy $output_file
}