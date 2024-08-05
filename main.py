import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'plastik\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah plastik')
                await ctx.send('ini merupakan sampah anorganik, cukup berbahaya apabila dibiarkan')
                await ctx.send('tetapi sampah ini bisa di daur ulang!!')
            elif hasil[0] == 'kaleng\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah kaleng')
                await ctx.send('in merupakan sampah anorganik, cukup berbahaya apabila dibiarkan')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'kaca\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah kaca')
                await ctx.send('ini merupakan sampah anorganik, sampah ini cukup berbahaya apabila dibiarkan')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'botol plastik\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah botol plastik')
                await ctx.send('ini merupakan sampah anorganik, cukup berbahaya apabila dibiarkan')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'kertas\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah kertas')
                await ctx.send('ini merupakan sampah organik, tidak terlalu berbahaya karna sampah ini mudah hancur')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'kardus\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah kardus')
                await ctx.send('ini merupakan sampah organik, tidak terlalu berbahaya karna mudah hancur')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'ban\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah ban')
                await ctx.send('ini merupakan sampah anorganik, cukup berbahaya apabila dibiarkan')
                await ctx.send('tetapi sampah ini bisa di daur ulang')
            elif hasil[0] == 'rokok\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah sampah rokok')
                await ctx.send('ini merupakan sampah anorganik yang sangat berbahaya apabila dibiarkan')
                await ctx.send('sampah ini tidak bisa di daur ulang karna sangat berbahaya bagi lingkungan dan kesehatan!!')
            else:
                await ctx.send('GAMBAR MU KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send('KIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('GAMBAR TIDAK VALID/GAADA >:/')

@bot.command()
async def checkAI(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            namafile = file.filename
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')
    
            kelas,skor = get_class('keras_model.h5','labels.txt',namafile)
    
            if kelas == 'motor\n' and skor >= 0.75:
                await ctx.send('ini adalah motor')
                await ctx.send('Sepeda motor biasanya menghasilkan antara 50 hingga 150 gram CO2 per kilometer (g/km')
                await ctx.send('harganya sangat murah dapat di beli di toko olah raga atau alat musik')
                await ctx.send('Emisi NOx dari sepeda motor bisa berkisar antara 0,05 hingga 0,5 gram per kilometer')
                await ctx.send('Emisi partikel (PM) dari sepeda motor biasanya sangat rendah dibandingkan dengan kendaraan diesel. Emisi PM biasanya berkisar antara 0,001 hingga 0,01 gram per kilometer')
                await ctx.send('Sepeda motor cenderung menghasilkan lebih banyak HC dan CO dibandingkan mobil. Emisi HC bisa berkisar antara 0,1 hingga 2 gram per kilometer, sementara emisi CO bisa berkisar antara 1 hingga 10 gram per kilometer')

            elif kelas == 'bajaj\n' and skor >= 0.75:
                await ctx.send('ini adalah gitar bajaj')
                await ctx.send('Emisi NOx dari bajaj bisa berkisar antara 0,05 hingga 1 gram per kilomete')
                await ctx.send('Emisi Karbon Dioksida (CO2) Bajaj yang menggunakan mesin bensin biasanya menghasilkan antara 70 hingga 150 gram CO2 per kilometer (g/km)')
                await ctx.send('Emisi partikel (PM) dari bajaj bisa berkisar antara 0,01 hingga 0,1 gram per kilometer, terutama jika bajaj tersebut menggunakan mesin diesel atau berbahan bakar campuran minyak dan bensin (seperti pada beberapa model dua tak)')
                await ctx.send('Bajaj dengan mesin bensin atau dua tak biasanya menghasilkan lebih banyak HC dan CO. Emisi HC bisa berkisar antara 0,1 hingga 2 gram per kilometer, dan emisi CO bisa berkisar antara 1 hingga 10 gram per kilometer.')

            elif kelas == 'mobil\n' and skor >= 0.75:
                await ctx.send('ini adalah mobil')
                await ctx.send('Mobil Bensin: Rata-rata mobil bensin menghasilkan sekitar 120 hingga 180 gram CO2 per kilometer (g/km)')
                await ctx.send('Mobil Bensin: Emisi NOx dari mobil bensin berkisar antara 0,01 hingga 0,05 gram per kilometer')
                await ctx.send('Mobil Bensin: Emisi partikel dari mobil bensin biasanya sangat rendah, sekitar 0,001 hingga 0,005 gram per kilometer.')
                await ctx.send('Mobil Bensin: Emisi HC dari mobil bensin berkisar antara 0,01 hingga 0,1 gram per kilometer, dan emisi CO bisa berkisar antara 0,1 hingga 2 gram per kilometer.')

            elif kelas == 'truk\n' and skor >= 0.75:
                await ctx.send('ini adalah truk')
                await ctx.send('Truk diesel besar biasanya menghasilkan antara 500 hingga 1.500 gram CO2 per kilometer (g/km), ')
                await ctx.send('Emisi NOx dari truk diesel bisa berkisar antara 0,5 hingga 10 gram per kilometer, tergantung pada usia truk dan standar emisi yang dipatuhi')
                await ctx.send('Emisi partikel (PM) dari truk diesel biasanya berkisar antara 0,01 hingga 1 gram per kilometer')
                await ctx.send('Emisi HC dan CO dari truk diesel biasanya lebih rendah dibandingkan dengan kendaraan bensin')

    else:
        await ctx.send('mana nih gambarnya?????')

bot.run('masukkan code mu kesini')
