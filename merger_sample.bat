@echo off
rem Pythonスクリプトを呼び出してテンプレートとコンテンツをマージする
rem コマンドプロンプトの文字コードをUTF-8に設定する
rem サンプルのHTMLファイルをビルドして生成する
chcp 65001 >nul

python merger.py template_sample.html page_content/_sample.html sample.html "サンプル"

