#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle("Player de Vídeo");

    Player = new QMediaPlayer();
    audioOutput = new QAudioOutput(this);
    audioOutput->setVolume(0.3); // 30% do volume máximo
    Player->setAudioOutput(audioOutput);


    ui->pushButton_play_pause->setIcon(style()->standardIcon(QStyle::SP_MediaPlay));
    ui->pushButton_stop->setIcon(style()->standardIcon(QStyle::SP_MediaStop));
    ui->pushButton_seek_backward->setIcon(style()->standardIcon(QStyle::SP_MediaSeekBackward));
    ui->pushButton_seek_forward->setIcon(style()->standardIcon(QStyle::SP_MediaSeekForward));
    ui->pushButton_volume->setIcon(style()->standardIcon(QStyle::SP_MediaVolume));

    ui->horizontalSlider_volume->setRange(0, 100);
    ui->horizontalSlider_volume->setValue(30);  // Inicia com volume 30

    connect(Player, &QMediaPlayer::durationChanged, this, &MainWindow::durationChanged);
    connect(Player, &QMediaPlayer::positionChanged, this, &MainWindow::positionChanged);

    ui->horizontalSlider_duration->setRange(0,Player->duration() / 1000);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::durationChanged(qint64 Duration)
{
    mDuration = Duration / 1000;
    ui->horizontalSlider_duration->setMaximum(mDuration);

}

void MainWindow::positionChanged(qint64 Duration)
{
    if(!ui->horizontalSlider_duration->isSliderDown()){
        ui->horizontalSlider_duration->setValue(Duration/1000);
    }

    updateDuration(Duration/1000);
}


void MainWindow::updateDuration(qint64 Duration)
{
    if (Duration || mDuration){

        QTime CurrentTime ((Duration/3600) % 60, (Duration/60)%60, Duration%60 , (Duration * 1000) % 1000 );
        QTime TotalTime ((mDuration/3600) % 60, (mDuration/60)%60, mDuration%60 ,(mDuration * 1000) % 1000 );

        QString Format = "";

        if(mDuration > 3600){
            Format = "hh:mm:ss";
        }
        else{
            Format = "mm:ss";
        }


        ui->label_current_time->setText(CurrentTime.toString((Format)));
        ui->label_total_time->setText(TotalTime.toString((Format)));

    }
}

void MainWindow::on_horizontalSlider_duration_valueChanged(int value)
{
    Player->setPosition(value*1000);
}



void MainWindow::on_pushButton_play_pause_clicked()
{
    if (Player->playbackState() == QMediaPlayer::PlayingState) {
        Player->pause();
        ui->pushButton_play_pause->setIcon(style()->standardIcon(QStyle::SP_MediaPlay));
    } else {
        Player->play();
        ui->pushButton_play_pause->setIcon(style()->standardIcon(QStyle::SP_MediaPause));
    }
}


void MainWindow::on_pushButton_stop_clicked()
{
    Player->stop();
}


void MainWindow::on_pushButton_volume_clicked()
{
    if(IS_Muted == false){
        IS_Muted = true;
        ui->pushButton_volume->setIcon(style()->standardIcon(QStyle::SP_MediaVolumeMuted));
        audioOutput->setMuted(true);
    }
    else{
        IS_Muted = false;
        ui->pushButton_volume->setIcon(style()->standardIcon(QStyle::SP_MediaVolume));
        audioOutput->setMuted(false);
    }
}


void MainWindow::on_horizontalSlider_volume_valueChanged(int value)
{
    // Converte o valor do slider (0-100) para um valor entre 0.0 e 1.0
    qreal linearVolume = QAudio::convertVolume(value / qreal(100.0),
                                               QAudio::LogarithmicVolumeScale,
                                               QAudio::LinearVolumeScale);

    // Define o volume do audioOutput
    audioOutput->setVolume(linearVolume);

    // Atualiza o ícone do botão de volume
    if (value == 0) {
        ui->pushButton_volume->setIcon(style()->standardIcon(QStyle::SP_MediaVolumeMuted));
        IS_Muted = true;
    } else {
        ui->pushButton_volume->setIcon(style()->standardIcon(QStyle::SP_MediaVolume));
        IS_Muted = false;
    }
}


void MainWindow::on_actionOpen_triggered()
{
    QString FileName = QFileDialog::getOpenFileName(this, tr("Select Video File"),"",tr("MP4 Files (*.mp4)"));

    if (FileName.isEmpty())
        return;

    Video = new QVideoWidget;
    Video->setGeometry(5,5,ui->groupBox_video->width() - 10,ui->groupBox_video->height() - 10);
    Video->setParent(ui->groupBox_video);

    Player->setVideoOutput(Video);
    Player->setSource(QUrl::fromLocalFile(FileName));
    Player->setAudioOutput(audioOutput);

    connect(Player, &QMediaPlayer::durationChanged, this, &MainWindow::onDurationChanged);
    connect(Player, &QMediaPlayer::positionChanged, this, &MainWindow::onPositionChanged);

    Video->setVisible(true);
    Video->show();

    Player->play();
}

void MainWindow::onDurationChanged(qint64 duration)
{
    ui->horizontalSlider_duration->setMaximum(duration / 1000);
}

void MainWindow::onPositionChanged(qint64 position)
{
    if (!ui->horizontalSlider_duration->isSliderDown())
        ui->horizontalSlider_duration->setValue(position / 1000);
}





void MainWindow::on_pushButton_seek_backward_clicked()
{
    ui->horizontalSlider_duration->setValue(ui->horizontalSlider_duration->value() - 20);
    Player->setPosition(ui->horizontalSlider_duration->value()*1000);
}


void MainWindow::on_pushButton_seek_forward_clicked()
{
    ui->horizontalSlider_duration->setValue(ui->horizontalSlider_duration->value() + 20);
    Player->setPosition(ui->horizontalSlider_duration->value()*1000);
}

