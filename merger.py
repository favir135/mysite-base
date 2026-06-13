import sys


def build(template_path, content_path, output_path, title):
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = template.replace('{{ title }}', title).replace(
        '{{ content }}', content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Build complete: {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("使い方: python build.py template.html content.html output.html 'タイトル'")
        sys.exit(1)

    build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
