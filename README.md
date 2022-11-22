#### Логика работы скрипта
 - Определяет директорию, в которой он сейчас находиться
 - Создаёт в этой директории следующие каталоги:
   1. Видео
   2. Фото
   3. Аудио
   4. Документы
   5. Архивы
- Сканирует файлы, находящиеся в директории и производит сортировку по созданным папкам, опираясь на расширение файла.
  Скрипт распознаёт расширения:
  > mp4, mov, avi, mkv, wmv, 3gp, 3g2, mpg, mpeg, m4v, h264, flv, rm, swf, vob, jpg, png, bmp, ai, psd, ico, jpeg, ps, svg, tif, tiff, gif, mp3, wav, ogg, flac, aif, mid, midi, mpa, wma, wpl, cda, pdf, txt, doc, docx, rtf, tex, wpd, odt, xlsx, xls, xlsm, ods, pptx, ppt, pps, key, odp, zip, rar, 7z, z, gz, rpm, arj, pkg, deb
- Сканирует каталоги, расположенные в директории. Если каталог пуст, производит его удаление.