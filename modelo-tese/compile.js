const latex = require('node-latex')
const fs = require('fs')

const input = fs.createReadStream('/home/alexandre/projetos/mestrado-unifesp/modelo-tese/primeiro.tex')
const output = fs.createWriteStream('/home/alexandre/projetos/mestrado-unifesp/modelo-tese/primeiro.pdf')
const pdf = latex(input)

pdf.pipe(output)
pdf.on('error', err => console.error(err))
pdf.on('finish', () => console.log('PDF generated!'))